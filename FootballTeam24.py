import streamlit as st

# Title of the app
st.title("Football Team Management App")

# Sidebar for user inputs
st.sidebar.header("Add a New Player")

# Function to add a new player
def add_player(name, position, number):
    if "players" not in st.session_state:
        st.session_state.players = []
    st.session_state.players.append({"name": name, "position": position, "number": number})

# Input fields in the sidebar
name = st.sidebar.text_input("Player Name")
position = st.sidebar.selectbox("Position", ["Goalkeeper", "Defender", "Midfielder", "Forward"])
number = st.sidebar.number_input("Jersey Number", min_value=1, max_value=99, step=1)

# Button to add the player
if st.sidebar.button("Add Player"):
    add_player(name, position, number)
    st.sidebar.success(f"Added {name} as a {position}")

# Display the team roster
st.header("Team Roster")

if "players" in st.session_state and st.session_state.players:
    for player in st.session_state.players:
        st.subheader(f"{player['name']} - {player['position']}")
        st.text(f"Jersey Number: {player['number']}")
else:
    st.text("No players added yet.")

# Additional functionality (optional)
st.sidebar.header("Remove a Player")
player_to_remove = st.sidebar.selectbox("Select Player to Remove", [player["name"] for player in st.session_state.get("players", [])])

if st.sidebar.button("Remove Player"):
    st.session_state.players = [player for player in st.session_state.players if player["name"] != player_to_remove]
    st.sidebar.success(f"Removed {player_to_remove}")
