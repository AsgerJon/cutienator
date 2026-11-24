//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideotransformation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideotransformation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void VideoTransformation::rotate(QtVideo::Rotation rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19VideoTransformation6rotateEN7QtVideo8RotationE(
    VideoTransformation *self,
    QtVideo::Rotation rotation) {
  self->rotate(rotation);
}

//  void VideoTransformation::mirrorHorizontally(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN19VideoTransformation18mirrorHorizontallyEb(
    VideoTransformation *self,
    bool mirror) {
  self->mirrorHorizontally(mirror);
}

//  void VideoTransformation::mirrorVertically(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN19VideoTransformation16mirrorVerticallyEb(
    VideoTransformation *self,
    bool mirror) {
  self->mirrorVertically(mirror);
}

//  int VideoTransformation::rotationIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19VideoTransformation13rotationIndexEv(
    const VideoTransformation *self) {
  return self->rotationIndex();
}

//  void VideoTransformation::appendRotation(quint32 angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN19VideoTransformation14appendRotationEj(
    VideoTransformation *self,
    quint32 angle) {
  self->appendRotation(angle);
}

//  VideoTransformation::~VideoTransformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19VideoTransformationD1Ev(VideoTransformation *self) {
  delete self;
}
