{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python311Packages.manim
  ];
  shellHook = ''
  '';
}
