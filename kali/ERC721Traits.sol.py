ERC721Traits.sol

// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.5.0;

import "https://gist.github.com/netpoe/d2361f1937650265e0677e9d23ae8cab#file-erc721flattened-sol";

import "./ERC721Flattened.sol";

contract WAAWSBTTrait is ERC721Full {
  
  //For SBT, create an array of traits to keep track of different traits
  //no traits can be the same
  string[] 
  public trait;
  mapping(string => bool) _traitExists;

 //constructor for an ERC721 is a name and symbol
  constructor() ERC721Full("WINNER", "HORSE") 
  
  public {
  }

  
  //create a new token by calling the mint function
  //every token needs to be different
  //need to pass in a trait that does not exist
  function createNFT(
      string memory _trait) 
  
  public {
    
    //check the mapping to determine if trait exists
    require(!_traitExists[_trait]);
    
    //if trait does not exist mint token and create a new token id
    //mint for the msg.sender
    //add trait to array and set trait in mapping to true
    uint _id = trait.push(_trait);
    _mint(msg.sender, _id);
    _traitExists[_trait] = true;
  }

}