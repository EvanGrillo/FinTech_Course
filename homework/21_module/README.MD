# Unit 21: Blockchain with Solidity, Ganache & Metamask

This unit covers writing a smart contract and enhancing its functionality with Open Zeppelin to inherit utility methods.

### Deploying the Crowdsale Deployer Contract

- **Symbol**: KC
- **Contract Owner Wallet Address**: `0xE9B5A7B8bE0C738D1D14873Fb189bA6221f9a358`
- **Goal**: Raise 100 ETHER worth of KC coin within 1 hour

#### Link Contracts and Buy Tokens:

- Utilize the 'At Address' field to link other contracts to their respective addresses.

- Three out of four accounts use `buyTokens` method to purchase 10 Ether worth of tokens.

##### Transaction Details:

- **Goal Reached**: `false`  
  ![Goal Reached Check](/Images/1_goal_reached.png)

- **Wei Raised**: `30000000000000000000 wei`, or `30 Ether`  
  ![Wei Raised](/Images/1_wei_raised.png)

- **Latest Balance**:  
  ![Latest Balance](/Images/latest_ether.png)

The crowdsale's deadline is set to the current (latest) Unix timestamp plus 1 hour. The `isOpen` method returns `true`, indicating the sale is currently active, while `hasClosed` returns `false`, showing it hasn't ended yet.

#### Checking Contract State:

To determine if the contract is open or closed, you can reference the Open Zeppelin's source code methods below:

```solidity
function isOpen() public view returns (bool) {
    // solhint-disable-next-line not-rely-on-time
    return block.timestamp >= _openingTime && block.timestamp <= _closingTime;
}

function hasClosed() public view returns (bool) {
    // solhint-disable-next-line not-rely-on-time
    return block.timestamp > _closingTime;
} 
```

The contract interface in Remix includes several buttons and fields to trigger transactions or check the latest contract state:
  ![Contract State](/Images/contract_interface.png)