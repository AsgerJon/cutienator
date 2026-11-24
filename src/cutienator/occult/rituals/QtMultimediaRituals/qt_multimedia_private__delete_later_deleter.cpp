//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmultimediautils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmultimediautils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QtMultimediaPrivate::DeleteLaterDeleter::operator()(QObject *ptr)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QtMultimediaPrivate18DeleteLaterDeleterclEP7QObject(
    const QtMultimediaPrivate::DeleteLaterDeleter *self,
    QObject *ptr) {
  self->operator()(ptr);
}

//  QtMultimediaPrivate::DeleteLaterDeleter::~DeleteLaterDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate18DeleteLaterDeleterD1Ev(
    QtMultimediaPrivate::DeleteLaterDeleter *self) {
  delete self;
}
