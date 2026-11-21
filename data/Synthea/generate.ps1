# Synthea release: release <v4.0.0>, downloaded 2026-11-18
# Generates one folder per state, each with its own fixed seed.
$jar = "synthea-with-dependencies.jar"

$runs = @(
    @{ State = "Massachusetts"; Seed = 42; Pop = 2000 },
    @{ State = "Texas";         Seed = 43; Pop = 1500 },
    @{ State = "Florida";       Seed = 44; Pop = 1500 }
)

foreach ($r in $runs) {
    $out = "./output/$($r.State.ToLower())/"
    Write-Host "Generating $($r.Pop) patients for $($r.State) into $out"
    java -jar $jar -s $r.Seed -cs $r.Seed -p $r.Pop -r 20260101 `
        --exporter.csv.export true --exporter.fhir.export false `
        --exporter.baseDirectory $out $r.State
}