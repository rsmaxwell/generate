package basic

// Version function
func Version() string {
	return "{{ build.id }}"
}

// BuildTime function
func BuildTime() string {
	return "{{ build.time }}"
}

// GitCommit function
func GitCommit() string {
	return "{{ git.commit }}"
}

// GitBranch function
func GitBranch() string {
	return "{{ git.branch }}"
}

// GitURL function
func GitURL() string {
	return "{{ git.url }}"
}