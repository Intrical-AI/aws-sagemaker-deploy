def generate_docker_image_tag(registry_uri, bento_name, bento_version):
    # image_tag = f"{bento_name}-{bento_version}".lower()
    image_tag = "latest"
    return f"{registry_uri}:{image_tag}"
