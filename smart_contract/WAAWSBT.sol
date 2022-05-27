pragma solidity ^0.8.2;

//import Open Zepplin contracts
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Strings.sol";

contract NFT is ERC721 {
    uint256 private _tokenIds;
    
    constructor() ERC721("Name", "Symbol") {}

    // needs to be unlocked for the `_mint()` function in constructor
    bool locked = false;

    function setLocked(bool _locked) external {
        locked = _locked;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(!locked, "Cannot transfer - currently locked");
    }




//use the mint function to create an NFT
    function mint()
    public
    returns (uint256)
    {
        
        
        _tokenIds += 1;
        _mint(msg.sender, _tokenIds);
        return _tokenIds;
    }
    




//in the function below include the CID of the JSON folder on IPFS
    function tokenURI(uint256 _tokenId) override public pure returns(string memory) {
        return string(
            abi.encodePacked(
                "",
                Strings.toString(_tokenId),
                ".json"
            )
        );
    }
}