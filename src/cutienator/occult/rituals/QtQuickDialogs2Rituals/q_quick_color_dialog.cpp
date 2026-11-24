//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickcolordialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickcolordialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickColorDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickColorDialog : QQuickColorDialog {
  using QQuickColorDialog::useNativeDialog;
  using QQuickColorDialog::onCreate;
  using QQuickColorDialog::onShow;
};

//  const QMetaObject *QQuickColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickColorDialog10metaObjectEv(
    const QQuickColorDialog *self) {
  return self->metaObject();
}

//  QString QQuickColorDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickColorDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickColorDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN17QQuickColorDialog20qmlExtendedNamespaceEv() {
  return QQuickColorDialog::qmlExtendedNamespace();
}

//  void QQuickColorDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickColorDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickColorDialog::QQuickColorDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickColorDialog *ritual_ZN17QQuickColorDialogC1EP7QObject(
    QObject *parent) {
  return new QQuickColorDialog(parent);
}

//  QColor QQuickColorDialog::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickColorDialog13selectedColorEv(
    const QQuickColorDialog *self) {
  return new QColor(self->selectedColor());
}

//  void QQuickColorDialog::setSelectedColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog16setSelectedColorERK6QColor(
    QQuickColorDialog *self,
    const QColor *color) {
  self->setSelectedColor(*color);
}

//  QColorDialogOptions::ColorDialogOptions QQuickColorDialog::options()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickColorDialog7optionsEv(const QQuickColorDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void
//      QQuickColorDialog::setOptions(QColorDialogOptions::ColorDialogOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog10setOptionsE6QFlagsIN19QColorDialogOptions17ColorDialogOptionEE(
    QQuickColorDialog *self,
    int options) {
  self->setOptions(
      QFlags<QColorDialogOptions::ColorDialogOption>::fromInt(options));
}

//  void QQuickColorDialog::resetOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog12resetOptionsEv(QQuickColorDialog *self) {
  self->resetOptions();
}

//  bool QQuickColorDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickColorDialog15useNativeDialogEv(
    const QQuickColorDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickColorDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog8onCreateEP21QPlatformDialogHelper(
    QQuickColorDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickColorDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorDialog6onShowEP21QPlatformDialogHelper(
    QQuickColorDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  bool QQuickColorDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QQuickColorDialog15useNativeDialogEv(
    const QQuickColorDialog *self) {
  return static_cast<const OwnQQuickColorDialog *>(self)->OwnQQuickColorDialog::useNativeDialog();
}

//  void QQuickColorDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickColorDialog8onCreateEP21QPlatformDialogHelper(
    QQuickColorDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickColorDialog *>(self)->OwnQQuickColorDialog::onCreate(
      dialog);
}

//  void QQuickColorDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickColorDialog6onShowEP21QPlatformDialogHelper(
    QQuickColorDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickColorDialog *>(self)->OwnQQuickColorDialog::onShow(
      dialog);
}
