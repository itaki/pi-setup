#!/bin/zsh

# Directory to install fonts
FONT_DIR="/usr/local/share/fonts"

# URLs for each font file
FONT_URLS=(
    "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf"
    "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf"
    "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf"
    "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf"
)

# Create the fonts directory if it doesn't exist
if [[ ! -d $FONT_DIR ]]; then
    echo "Creating font directory at $FONT_DIR"
    sudo mkdir -p $FONT_DIR
fi

# Download and install each font
for FONT_URL in $FONT_URLS; do
    FONT_FILE="${FONT_URL:t}"  # Extract the filename from the URL
    DEST="$FONT_DIR/$FONT_FILE"
    
    echo "Downloading $FONT_FILE..."
    sudo curl -L -o "$DEST" "$FONT_URL"
    
    if [[ -f $DEST ]]; then
        echo "Successfully installed $FONT_FILE in $FONT_DIR"
    else
        echo "Failed to download $FONT_FILE"
    fi
done

# Update font cache
echo "Updating font cache..."
sudo fc-cache -f -v

echo "Font installation complete!"