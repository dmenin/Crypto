var ChainList = artifacts.require("./ChainList.sol");//loads the contract

module.exports = function(deployer) {
  deployer.deploy(ChainList);
};
