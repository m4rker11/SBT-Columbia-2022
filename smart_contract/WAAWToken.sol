pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
// // import "./ERC721.sol";
// import "./ERC721Enumerable.sol";
// import "./ERC721Metadata.sol";

/**
 * @title Full ERC721 Token
 * @dev This implementation includes all the required and some optional functionality of the ERC721 standard
 * Moreover, it includes approve all functionality using operator terminology.
 *
 * See https://eips.ethereum.org/EIPS/eip-721
 */

contract WAAWToken is ERC721Full {

    constructor() public ERC721Full("WAAWTokenName", "WAAWTokenSymbol") { }

    function awardWAAWTokenName(address studentAddress, string memory tokenURI) public returns (uint) {
        // uses total supply function from ERC721Enumerable to create a counter; start at 0 and goes up
        uint newWAAWTokenID = totalSupply();

        // generate token using the WAAWTokenName ID generated one line above
        _mint(studentAddress, newWAAWTokenID);

        // making the connection between the certificate and the tokenURI
        _setTokenURI(newWAAWTokenID, tokenURI);

        // return the unique id for the newWAAWTokenID
        return newWAAWTokenID;

    }

}