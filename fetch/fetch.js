// let player = fetch('https://api.gametools.network/bf4/stats/?format_values=true&name=iiTzArcur&playerid=794397421&platform=pc')
// console.log(player)

async function player() {
  const response = await fetch("https://api.gametools.network/bf4/stats/?format_values=true&name=iiTzArcur&playerid=794397421&platform=pc");
  const playerStat = await response.json();
  console.log(playerStat);
}
player()
