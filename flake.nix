{
  description = "Infrastructure layer for pythoneda-artifact/base";

  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";
    poetry2nix = {
      url = "github:nix-community/poetry2nix/v1.28.0";
      inputs.nixpkgs.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
    };
    pythoneda-base = {
      url = "github:pythoneda/base/0.0.1a12";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.poetry2nix.follows = "poetry2nix";
    };
    pythoneda-artifact-base = {
      url = "github:pythoneda-artifact/base/0.0.1a1";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.poetry2nix.follows = "poetry2nix";
      inputs.pythoneda-base.follows = "pythoneda-base";
    };
  };
  outputs = inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        description = "Infrastructure layer for pythoneda-artifact/base";
        license = pkgs.lib.licenses.gpl3;
        homepage = "https://github.com/pythoneda-artifact-infrastructure/base";
        maintainers = with pkgs.lib.maintainers; [ ];
        nixpkgsRelease = "nixos-23.05";
        shared = import ./nix/devShell.nix;
        pythoneda-artifact-infrastructure-base-for =
          { version, pythoneda-base, pythoneda-artifact-base, python }:
          python.pkgs.buildPythonPackage rec {
            pname = "pythoneda-artifact-infrastructure-base";
            inherit version;
            projectDir = ./.;
            src = ./.;
            format = "pyproject";

            nativeBuildInputs = with python.pkgs; [ pip poetry-core ];
            propagatedBuildInputs = with python.pkgs; [
              pythoneda-base
              pythoneda-artifact-base
            ];

            checkInputs = with python.pkgs; [ pytest ];

            pythonImportsCheck = [ "pythonedaartifactinfrastructure" ];

            preBuild = ''
              python -m venv .env
              source .env/bin/activate
              pip install ${pythoneda-base}/dist/pythoneda_base-0.0.1a12-py3-none-any.whl
              pip install ${pythoneda-artifact-base}/dist/pythoneda_artifact_base-0.0.1a1-py3-none-any.whl
            '';

            postInstall = ''
              mkdir $out/dist
              cp dist/*.whl $out/dist
            '';

            meta = with pkgs.lib; {
              inherit description license homepage maintainers;
            };
          };
        pythoneda-artifact-infrastructure-base-0_0_1a1-for =
          { pythoneda-base, pythoneda-artifact-base, python }:
          pythoneda-artifact-infrastructure-base-for {
            version = "0.0.1a1";
            inherit pythoneda-base pythoneda-artifact-base python;
          };
      in rec {
        packages = rec {
          pythoneda-artifact-infrastructure-base-0_0_1a1-python38 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
              pythoneda-artifact-base =
                pythoneda-artifact-base.packages.${system}.pythoneda-artifact-base-latest-python38;
              python = pkgs.python38;
            };
          pythoneda-artifact-infrastructure-base-0_0_1a1-python39 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python39;
              pythoneda-artifact-base =
                pythoneda-artifact-base.packages.${system}.pythoneda-artifact-base-latest-python39;
              python = pkgs.python39;
            };
          pythoneda-artifact-infrastructure-base-0_0_1a1-python310 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
              pythoneda-artifact-base =
                pythoneda-artifact-base.packages.${system}.pythoneda-artifact-base-latest-python310;
              python = pkgs.python310;
            };
          pythoneda-artifact-infrastructure-base-latest-python38 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python38;
          pythoneda-artifact-infrastructure-base-latest-python39 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python39;
          pythoneda-artifact-infrastructure-base-latest-python310 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python310;
          pythoneda-artifact-infrastructure-base-latest =
            pythoneda-artifact-infrastructure-base-latest-python310;
          default = pythoneda-artifact-infrastructure-base-latest;
        };
        defaultPackage = packages.default;
        devShells = rec {
          pythoneda-artifact-infrastructure-base-0_0_1a1-python38 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-infrastructure-base-0_0_1a1-python38;
              python = pkgs.python38;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-infrastructure-base-0_0_1a1-python39 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-infrastructure-base-0_0_1a1-python39;
              python = pkgs.python39;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-infrastructure-base-0_0_1a1-python310 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-infrastructure-base-0_0_1a1-python310;
              python = pkgs.python310;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-infrastructure-base-latest-python38 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python38;
          pythoneda-artifact-infrastructure-base-latest-python39 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python39;
          pythoneda-artifact-infrastructure-base-latest-python310 =
            pythoneda-artifact-infrastructure-base-0_0_1a1-python310;
          pythoneda-artifact-infrastructure-base-latest =
            pythoneda-artifact-infrastructure-base-latest-python310;
          default = pythoneda-artifact-infrastructure-base-latest;

        };
      });
}
