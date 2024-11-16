{
  inputs = {
    # nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs =
    { systems, nixpkgs, ... }@inputs:
    let
      eachSystem = f: nixpkgs.lib.genAttrs (import systems) (system: f nixpkgs.legacyPackages.${system});
    in
    {
      devShells = eachSystem (pkgs: {
        default = pkgs.mkShell {
          buildInputs = [
            pkgs.python3
            pkgs.python312Packages.pip

            # You can set the major version of Node.js to a specific one instead
            # of the default version
            # pkgs.nodejs-22_x

            # It is possible to use bun instead of node.
            # pkgs.bun

            # Optionally, you can add yarn or pnpm for package management for node.
            # pkgs.nodePackages.pnpm
            # pkgs.yarn
          ];

          shellHook = ''
          echo "Welcome to Yunzdle API Dev Shell"
          '';
        };
      });
    };
}
