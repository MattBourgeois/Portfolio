var perks = [
    "Bond", "Prove Thyself", "Leader",
    "Empathy", "Botany Knowledge", "Self-care",
    "Balanced Landing", "Urban Evasion", "Streetwise",
    "Open-Handed", "Up the Ante", "Ace in the Hole",
    "Technician", "Lithe", "Alert",
    "Wake Up!", "Pharmacy", "Vigil" ,
    "Dance With Me", "Windows of Opportunity", "Boil Over",
    "Breakdown", "Aftercare", "Distortion",
    "Flip-Flop", "Buckle Up", "Mettle of Man",
    "Guardian", "Kinship", "Second Wind",
    "Off the Record", "Red Herring", "For the People",
    "Visionary", "Desperate Measires", "Built to Last",
    "Fast Track", "Smash hit", "Self-Preservation",
    "Bite the Bullet", "Flashbang", "Rookie Spirt",
    "Overcome", "Corrective Action", "Expoential",
    "Quick & Quiet", "Sprint Burst", "Adrenaline",
    "Iron Will", "Calm Spirit", "Saboteur",
    "Sole Survivor", "Object of Obsession", "Decisive Strike",
    "Left Behind", "Borrowed Time", "Unbreakable",
    "We're Gonna Live Forever", "Dead Hard", "No Mither",
    "Tenacity", "Detective's Hunch", "Stake Out",
    "Diversion", "Deliverance", "Autodidact",
    "Solidarity", "Poised", "Head On",
    "Better Tigetger", "Self Aware", "Inner Strength",
    "Lucky Break", "Any Means Necessary", "Breakout",
    "Soul Guard", "Blood Pact", "Repressed Alliance",
    "Counterforce", "Resurgence", "Blast Mine",
    "Appraisal", "Deception", "Power Struggle",
    "Clairvoyance", "Circle of Healing", "Shadow Step",
    "Parental Guidance", "Empathic Connection", "Dark Theory",
    "Inner Focus", "Residual Mainfest", "Overzealous",
]

function fourperks(){
    for(var x = 0; x < 4; x++){
        i = Math.random() * 100
        console.log(Math.round(i))
        console.log(perks[i])
    }
}
fourperks(4)