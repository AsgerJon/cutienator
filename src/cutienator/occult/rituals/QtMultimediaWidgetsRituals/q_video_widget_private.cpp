//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaWidgets/6.12.0/QtMultimediaWidgets/private/qvideowidget_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtMultimediaWidgets/qvideowidget.h>
#include <QtMultimediaWidgets/QtMultimediaWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaWidgets/6.12.0/QtMultimediaWidgets/private/qvideowidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVideoWidget *QVideoWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QVideoWidget *ritual_ZN19QVideoWidgetPrivate6q_funcEv(
    QVideoWidgetPrivate *self) {
  return self->q_func();
}

//  const QVideoWidget *QVideoWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QVideoWidget *ritual_ZNK19QVideoWidgetPrivate6q_funcEv(
    const QVideoWidgetPrivate *self) {
  return self->q_func();
}

//  QVideoWidgetPrivate::~QVideoWidgetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWidgetPrivateD1Ev(QVideoWidgetPrivate *self) {
  delete self;
}
