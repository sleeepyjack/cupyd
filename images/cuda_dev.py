from __future__ import absolute_import
import modules.dev_env
import modules.cmake
import modules.cuda


def emit(writer, **kwargs):
    if "cudaVersion" not in kwargs:
        raise Exception("'cudaVersion' is mandatory!")
    cudaVersion = kwargs["cudaVersion"]
    modules.dev_env.emit(writer, **kwargs)
    modules.cmake.emit(writer, "3.21.0")
    _, _, versionShort, pkgVersion = modules.cuda.shortVersion(cudaVersion)
    short = float(versionShort)
    pkgs = ["zlib1g-dev"]
    if short >= 10.0:
        pkgs += [
            "cuda-nsight-compute-$pkgVersion",
            "cuda-nsight-systems-$pkgVersion",
        ]
    writer.packages(pkgs, pkgVersion=pkgVersion,
                    installOpts="--allow-downgrades")


def images():
    return {
        "cuda-dev:1804-102": {
            "cudaVersion": "10.2",
            "base": "nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04",
            "needsContext": True,
        },
        "cuda-dev:2004-112": {
            "cudaVersion": "11.2",
            "base": "nvidia/cuda:11.2.2-devel-ubuntu20.04",
            "needsContext": True,
        },
        "cuda-dev:2004-113": {
            "cudaVersion": "11.3",
            "base": "nvidia/cuda:11.3.1-devel-ubuntu20.04",
            "needsContext": True,
        },
        "cuda-dev:2004-114": {
            "cudaVersion": "11.4",
            "base": "nvidia/cuda:11.4.0-devel-ubuntu20.04",
            "needsContext": True,
        }
    }
