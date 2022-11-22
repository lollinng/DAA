// https://remix.ethereum.org/

// Ethernet
// https://goerli-faucet.pk910.de/
// https://ethdrop.dev/




# BANK EZ
pragma solidity 0.4.25;
contract Bank{

    int bal;

    constructor() public{
        bal = 1;
    }

    // the below function returns value and doesnt change value hence view
    function getBalance() view public returns(int){
        return bal;
    }

    function withdraw(int amt) public{
        bal = bal - amt;
    }

    function deposit(int amt) public{
        bal = bal + amt;
    }

}


# bank 
pragma solidity ^0.6;
contract banking
{
    mapping(address=>uint) private user_account;  // user_account dict is created with address and unit keys and values
    function deposit(uint amount) public payable returns(string memory)
    {
        user_account[msg.sender] += amount;
        return "Deposited Successfully";
    }
    function withdraw(uint amount) public payable returns(string memory)
    {
        require(user_account[msg.sender]>amount,"Insufficient Balance");
        require(amount>10,"Amount should be more than zero");
        user_account[msg.sender]=user_account[msg.sender]-amount;
        return "Withdrawl Successful";
    }
    function user_balance() public view returns(uint)
    {
        return user_account[msg.sender];
    }
}




REPORT-
https://www.simplilearn.com/tutorials/blockchain-tutorial/types-of-blockchain