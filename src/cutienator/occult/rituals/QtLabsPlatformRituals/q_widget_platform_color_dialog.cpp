//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformcolordialog_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(colordialog)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformcolordialog_p.h>
#include <QtGui/qcolor.h>
#include <QtGui/qwindow.h>

//  const QMetaObject *QWidgetPlatformColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWidgetPlatformColorDialog10metaObjectEv(
    const QWidgetPlatformColorDialog *self) {
  return self->metaObject();
}

//  QWidgetPlatformColorDialog::~QWidgetPlatformColorDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetPlatformColorDialogD1Ev(
    QWidgetPlatformColorDialog *self) {
  delete self;
}

//  QColor QWidgetPlatformColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QWidgetPlatformColorDialog12currentColorEv(
    const QWidgetPlatformColorDialog *self) {
  return new QColor(self->currentColor());
}

//  void QWidgetPlatformColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetPlatformColorDialog15setCurrentColorERK6QColor(
    QWidgetPlatformColorDialog *self,
    const QColor *color) {
  self->setCurrentColor(*color);
}

//  void QWidgetPlatformColorDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetPlatformColorDialog4execEv(
    QWidgetPlatformColorDialog *self) {
  self->exec();
}

//  bool QWidgetPlatformColorDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QWidgetPlatformColorDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QWidgetPlatformColorDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags), modality, parent);
}

//  void QWidgetPlatformColorDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetPlatformColorDialog4hideEv(
    QWidgetPlatformColorDialog *self) {
  self->hide();
}

#endif  // QT_CONFIG(colordialog)
