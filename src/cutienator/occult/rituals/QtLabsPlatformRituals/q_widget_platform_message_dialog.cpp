//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmessagedialog_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(messagebox)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmessagedialog_p.h>
#include <QtGui/qwindow.h>

//  const QMetaObject *QWidgetPlatformMessageDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QWidgetPlatformMessageDialog10metaObjectEv(
    const QWidgetPlatformMessageDialog *self) {
  return self->metaObject();
}

//  QWidgetPlatformMessageDialog::~QWidgetPlatformMessageDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWidgetPlatformMessageDialogD1Ev(
    QWidgetPlatformMessageDialog *self) {
  delete self;
}

//  void QWidgetPlatformMessageDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWidgetPlatformMessageDialog4execEv(
    QWidgetPlatformMessageDialog *self) {
  self->exec();
}

//  bool QWidgetPlatformMessageDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QWidgetPlatformMessageDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QWidgetPlatformMessageDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags), modality, parent);
}

//  void QWidgetPlatformMessageDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWidgetPlatformMessageDialog4hideEv(
    QWidgetPlatformMessageDialog *self) {
  self->hide();
}

#endif  // QT_CONFIG(messagebox)
