//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformfontdialog_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(fontdialog)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformfontdialog_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qwindow.h>

//  const QMetaObject *QWidgetPlatformFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QWidgetPlatformFontDialog10metaObjectEv(
    const QWidgetPlatformFontDialog *self) {
  return self->metaObject();
}

//  QWidgetPlatformFontDialog::~QWidgetPlatformFontDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFontDialogD1Ev(
    QWidgetPlatformFontDialog *self) {
  delete self;
}

//  QFont QWidgetPlatformFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK25QWidgetPlatformFontDialog11currentFontEv(
    const QWidgetPlatformFontDialog *self) {
  return new QFont(self->currentFont());
}

//  void QWidgetPlatformFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFontDialog14setCurrentFontERK5QFont(
    QWidgetPlatformFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}

//  void QWidgetPlatformFontDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFontDialog4execEv(
    QWidgetPlatformFontDialog *self) {
  self->exec();
}

//  bool QWidgetPlatformFontDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetPlatformFontDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QWidgetPlatformFontDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags), modality, parent);
}

//  void QWidgetPlatformFontDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetPlatformFontDialog4hideEv(
    QWidgetPlatformFontDialog *self) {
  self->hide();
}

#endif  // QT_CONFIG(fontdialog)
