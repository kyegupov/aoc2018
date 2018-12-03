use std::collections::BTreeSet;
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use std::io::Error;
use std::env;

fn main() -> Result<(), Error> {   

    match env::args().collect::<Vec<String>>()[1].as_ref() {
        "1" => main1(),
        "2" => main2(),
        _ => panic!()
    }
}   

fn main1() -> Result<(), Error> {   
    let file = BufReader::new(File::open("../input01")?);
    let mut s = 0;
    for line in file.lines() {
        let l = line.unwrap();
        s += l.parse::<i32>().unwrap();
    }
    println!("{}", s);
    Ok(())          
}

fn main2() -> Result<(), Error> {
    let mut s = 0;
    let mut ss = BTreeSet::new();
    loop {
        let file = BufReader::new(File::open("../input01")?);
        for line in file.lines() {
            let l = line.unwrap();
            s += l.parse::<i32>().unwrap();
            if ss.contains(&s) {
               println!("{}", s);
               return Ok(());
            }
            ss.insert(s);
        }
    }
    println!("{}", s);
    Ok(())          
}
