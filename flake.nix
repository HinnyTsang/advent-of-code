{
  description = "Python workspace";
  inputs = {
    flake-utils = { url = "github:numtide/flake-utils"; };
    nixpkgs = { url = "github:NixOS/nixpkgs/nixos-23.11"; };
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        poetry = pkgs.poetry.override {
          python3 = pkgs.python310;
        };
        buildInputs =
          [
            poetry
	    pkgs.zlib
	    pkgs.glibc
          ];
      in
      {
        devShells.default = pkgs.mkShell {
          name = "Project Shell";
          buildInputs = buildInputs;
	  shellHook = ''
	    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath buildInputs}:$LD_LIBRARY_PATH"
	    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib.outPath}/lib:$LD_LIBRARY_PATH"
	  '';
        };
      });
}
