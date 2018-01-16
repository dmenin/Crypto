pragma solidity ^0.4.11;

contract ChainList {
    // State variables
    address seller;
    string name;
    string description;
    uint256 price;

    // sell an article
    function sellArticle(string _name, string _description, uint256 _price) public {
        seller = msg.sender; //retrieve the address of the account calling the function
        name = _name;
        description = _description;
        price = _price;
    }

    // get the article - calling is free because it does not alter the state
    function getArticle() public constant returns (
        address _seller,
        string _name,
        string _description,
        uint256 _price) {
        return(seller, name, description, price);
    }
}
