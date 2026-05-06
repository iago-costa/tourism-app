# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Define the packages available in this shell environment
  packages = with pkgs; [
    # Node.js: Essential for running JavaScript code and the React Native CLI
    # You can choose a specific version like nodejs-18_x or nodejs-20_x
    nodejs_20

    # Yarn: A popular package manager often used in React Native projects
    yarn

    # --- Optional: Add packages needed for specific platforms ---

    # For Android development, you will need a Java Development Kit (JDK)
    # You might need a specific version depending on your React Native version
    # jdk # Default JDK
    # jdk17 # Specific version, often required

    # For iOS development on macOS, you will need CocoaPods
    # cocoaPods # Requires macOS
  ];

  # Define commands to run when entering the shell
  shellHook = ''
    echo "Entering React Native development environment."
    echo "Node.js version: $(node -v)"
    echo "Yarn version: $(yarn -v)"

    # --- Optional: Environment variables for Android SDK ---
    # Managing the Android SDK with Nix can be complex.
    # If you have the Android SDK installed manually (e.g., via Android Studio),
    # you might need to set environment variables like ANDROID_HOME.
    # Replace /path/to/your/android/sdk with the actual path.
    # export ANDROID_HOME="/path/to/your/android/sdk"
    # export PATH="$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin"
    # echo "ANDROID_HOME set to: $ANDROID_HOME"
  '';

  # Optional: Allow fetching unfree packages (like some Android SDK components)
  # allowUnfree = true;
}
