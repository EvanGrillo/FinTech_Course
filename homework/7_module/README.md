## Database Setup

#### Entity Relationship Diagram
![Entity Relationship Diagram](../Data/ERD.png)


#### [Analyze Data to Create Constraint](../Starter_Files/analyze_raw_data.ipynb)

#### Create Tables
```sql
CREATE TABLE card_holder (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE credit_card (
    card VARCHAR(20) PRIMARY KEY,
    cardholder_id INT REFERENCES card_holder(id),
);

CREATE TABLE merchant_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE merchant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    id_merchant_category INT REFERENCES merchant_category(id),
);

CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    amount NUMERIC,
    card VARCHAR(20) REFERENCES credit_card(card),
    id_merchant INT REFERENCES merchant(id),
);
```

## Report for CFO: Identifying Fraudulent Transactions with SQL

#### How can you isolate (or group) the transactions of each cardholder?

```sql
SELECT
    ch.name, 
    ROUND(SUM(tr.amount), 2) AS total_spend,
    ROUND(AVG(tr.amount), 2) AS avg_spend,
    ROUND(MIN(tr.amount), 2) AS min_spend,
    ROUND(MAX(tr.amount), 2) AS max_spend,
    cs.spend_count AS total_transactions_under_2
FROM transaction tr
INNER JOIN credit_card cc ON cc.card = tr.card
INNER JOIN card_holder ch ON ch.id = cc.cardholder_id
INNER JOIN (
    SELECT 
        COUNT(*) AS spend_count, 
        ch.id 
    FROM transaction tr_inner
    INNER JOIN credit_card cc_inner ON cc_inner.card = tr_inner.card
    INNER JOIN card_holder ch ON ch.id = cc_inner.cardholder_id
    WHERE tr_inner.amount < 2.00
    GROUP BY ch.id
) AS cs ON cs.id = ch.id
GROUP BY (ch.name, cs.spend_count)
ORDER BY total_transactions_under_2 DESC
```

#### Count the transactions that are less than $2.00 per cardholder.

```sql
SELECT ch.name, COUNT(tr.id) AS total_transactions_under_2,
FROM transaction tr
INNER JOIN credit_card cc on cc.card = tr.card
INNER JOIN card_holder ch on ch.id = cc.cardholder_id
WHERE tr.amount < 2.00
GROUP BY ch.name
ORDER BY total_transactions_under_2 DESC

-- Look at merchant data without aggregation
SELECT 
    TO_CHAR(CAST(tr.date AS DATE), 'Day'),
    tr.date, 
    tr.amount, 
    ch.name AS customer, 
    m.name AS merchant, 
    mc.name AS merchant_type
FROM transaction tr
INNER JOIN credit_card cc on cc.card = tr.card
INNER JOIN card_holder ch on ch.id = cc.cardholder_id
INNER JOIN merchant m on m.id = tr.id_merchant
INNER JOIN merchant_category mc on mc.id = m.id_merchant_category
WHERE tr.amount < 2.00
ORDER BY tr.date
```

#### Is there any evidence to suggest that a credit card has been hacked? Explain your rationale.

It's suspicious to see transactions that are less than $2 at some merchant types, particularly restaurants, pubs and bars. Even at food trucks and coffees (where we could assume have a lower average spend per transaction), these transactions are also worth investigating.

#### What are the top 100 highest transactions made between 7:00 am and 9:00 am?

```sql
SELECT 
    round(t.amount, 2) AS spend, 
    t.date, 
    TO_CHAR(t.date, 'Dy') AS day_of_week,
    ch.name AS customer,
    m.name AS merchant, 
    mc.name AS merchant_type 
FROM transaction t
INNER JOIN merchant m ON m.id = t.id_merchant
INNER JOIN merchant_category mc ON mc.id = m.id_merchant_category
INNER JOIN credit_card cc ON cc.card = t.card
INNER JOIN card_holder ch ON ch.id = cc.cardholder_id
WHERE t.date BETWEEN
    DATE_TRUNC('day', t.date) + INTERVAL '7 hours' AND
    DATE_TRUNC('day', t.date) + INTERVAL '9 hours'
ORDER BY t.amount DESC
LIMIT 100
```

#### Do you see any anomalous transactions that could be fraudulent?

Yes, some of the top transactions are unusual and could be fraudulent. 

#### Is there a higher number of fraudulent transactions made during this time frame versus the rest of the day?

Within the top ten transactions, there were occurrences of spend amounts exceeding $1,000 prior to 9am. While $1,000 transactions at bars and restaurants isn't suspicious, the timing of these transactions raises concerns.

There's a notable $1,000 spend at a coffee shop, which seems unusually high considering the merchant type.
