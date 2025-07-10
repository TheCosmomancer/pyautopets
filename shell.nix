{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs;[
    python313Packages.peewee
    python313Packages.pygame
  ];
}
