//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qarraydata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qarraydata.h>

//  CutResult QtPrivate::QContainerImplHelper::mid(qsizetype originalLength,
//      qsizetype *_position, qsizetype *_length)
extern "C" Q_DECL_EXPORT
QtPrivate::QContainerImplHelper::CutResult ritual_ZN9QtPrivate20QContainerImplHelper3midExPxS1_(
    qsizetype originalLength,
    qsizetype *_position,
    qsizetype *_length) {
  return QtPrivate::QContainerImplHelper::mid(
      originalLength,
      _position,
      _length);
}

//  QtPrivate::QContainerImplHelper::~QContainerImplHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QContainerImplHelperD1Ev(
    QtPrivate::QContainerImplHelper *self) {
  delete self;
}
