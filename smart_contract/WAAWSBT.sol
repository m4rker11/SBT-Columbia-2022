// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

//import Open Zepplin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract NFT is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private currentTokenId;
    
    constructor() ERC721("WAWToken", "WAWT") { }

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
        currentTokenId.increment();
        uint256 newItemId = currentTokenId.current();
        _mint(msg.sender, newItemId);
        return newItemId;
    }
    
//in the function below include the CID of the JSON folder on IPFS
    function tokenURI(uint256 _tokenId) override public pure returns(string memory) {
        return string(
            abi.encodePacked(
                "https://gateway.pinata.cloud/ipfs/QmdRsCBwY7sCwdXro41HrtqaqR18BGauDP8aNTm4Q9n8Ex/",
                Strings.toString(_tokenId),
                ".json"
            )
        );
    }
  
    // this event freezes the metadata so is no longer changeable by anyone
    event PermanentURI(string _value, uint256 indexed _id);
}