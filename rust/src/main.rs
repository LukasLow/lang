extern crate reqwest;

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    println!("Gib den Namen der Stadt ein:");
    
    let mut city = String::new();
    std::io::stdin().read_line(&mut city).expect("Fehler beim Lesen der Eingabe");
    let city = city.trim();

    let url = format!("https://wttr.in/{}?format=3", city);
    
    let response = reqwest::get(&url).await?;
    let body = response.text().await?;
    
    println!("Wetter in {}: {}", city, body);
    
    Ok(())
}
