//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcapturablewindow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcapturablewindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qcapturablewindow.h>

//  QCapturableWindowPrivate::QCapturableWindowPrivate(Id id, QString
//      &&description)
extern "C" Q_DECL_EXPORT
QCapturableWindowPrivate *ritual_ZN24QCapturableWindowPrivateC1EmO7QString(
    unsigned long long id,
    QString *description) {
  return new QCapturableWindowPrivate(id, std::move(*description));
}

//  const QCapturableWindowPrivate *QCapturableWindowPrivate::handle(const
//      QCapturableWindow &window)
extern "C" Q_DECL_EXPORT
const QCapturableWindowPrivate *ritual_ZN24QCapturableWindowPrivate6handleERK17QCapturableWindow(
    const QCapturableWindow *window) {
  return QCapturableWindowPrivate::handle(*window);
}

//  QCapturableWindow QCapturableWindowPrivate::create(Id id, QString
//      &&description)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN24QCapturableWindowPrivate6createEmO7QString(
    unsigned long long id,
    QString *description) {
  return new QCapturableWindow(
      QCapturableWindowPrivate::create(
          id,
          std::move(*description)));
}

//  QCapturableWindowPrivate::~QCapturableWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCapturableWindowPrivateD1Ev(
    QCapturableWindowPrivate *self) {
  delete self;
}
