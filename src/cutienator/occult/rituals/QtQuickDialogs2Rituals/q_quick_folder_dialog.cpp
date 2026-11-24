//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfolderdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfolderdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  Only a class built on QQuickFolderDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFolderDialog : QQuickFolderDialog {
  using QQuickFolderDialog::useNativeDialog;
  using QQuickFolderDialog::onCreate;
  using QQuickFolderDialog::onShow;
};

//  const QMetaObject *QQuickFolderDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickFolderDialog10metaObjectEv(
    const QQuickFolderDialog *self) {
  return self->metaObject();
}

//  QString QQuickFolderDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickFolderDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFolderDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickFolderDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN18QQuickFolderDialog20qmlExtendedNamespaceEv() {
  return QQuickFolderDialog::qmlExtendedNamespace();
}

//  void QQuickFolderDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickFolderDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickFolderDialog::QQuickFolderDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFolderDialog *ritual_ZN18QQuickFolderDialogC1EP7QObject(
    QObject *parent) {
  return new QQuickFolderDialog(parent);
}

//  QUrl QQuickFolderDialog::currentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickFolderDialog13currentFolderEv(
    const QQuickFolderDialog *self) {
  return new QUrl(self->currentFolder());
}

//  void QQuickFolderDialog::setCurrentFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog16setCurrentFolderERK4QUrl(
    QQuickFolderDialog *self,
    const QUrl *folder) {
  self->setCurrentFolder(*folder);
}

//  QUrl QQuickFolderDialog::selectedFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickFolderDialog14selectedFolderEv(
    const QQuickFolderDialog *self) {
  return new QUrl(self->selectedFolder());
}

//  void QQuickFolderDialog::setSelectedFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog17setSelectedFolderERK4QUrl(
    QQuickFolderDialog *self,
    const QUrl *folder) {
  self->setSelectedFolder(*folder);
}

//  QFileDialogOptions::FileDialogOptions QQuickFolderDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickFolderDialog7optionsEv(
    const QQuickFolderDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QQuickFolderDialog::setOptions(QFileDialogOptions::FileDialogOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog10setOptionsE6QFlagsIN18QFileDialogOptions16FileDialogOptionEE(
    QQuickFolderDialog *self,
    int options) {
  self->setOptions(
      QFlags<QFileDialogOptions::FileDialogOption>::fromInt(options));
}

//  void QQuickFolderDialog::resetOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog12resetOptionsEv(
    QQuickFolderDialog *self) {
  self->resetOptions();
}

//  QString QQuickFolderDialog::acceptLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickFolderDialog11acceptLabelEv(
    const QQuickFolderDialog *self) {
  return new QString(self->acceptLabel());
}

//  void QQuickFolderDialog::setAcceptLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog14setAcceptLabelERK7QString(
    QQuickFolderDialog *self,
    const QString *label) {
  self->setAcceptLabel(*label);
}

//  void QQuickFolderDialog::resetAcceptLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog16resetAcceptLabelEv(
    QQuickFolderDialog *self) {
  self->resetAcceptLabel();
}

//  QString QQuickFolderDialog::rejectLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickFolderDialog11rejectLabelEv(
    const QQuickFolderDialog *self) {
  return new QString(self->rejectLabel());
}

//  void QQuickFolderDialog::setRejectLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog14setRejectLabelERK7QString(
    QQuickFolderDialog *self,
    const QString *label) {
  self->setRejectLabel(*label);
}

//  void QQuickFolderDialog::resetRejectLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog16resetRejectLabelEv(
    QQuickFolderDialog *self) {
  self->resetRejectLabel();
}

//  bool QQuickFolderDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickFolderDialog15useNativeDialogEv(
    const QQuickFolderDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickFolderDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickFolderDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickFolderDialog6onShowEP21QPlatformDialogHelper(
    QQuickFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  bool QQuickFolderDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QQuickFolderDialog15useNativeDialogEv(
    const QQuickFolderDialog *self) {
  return static_cast<const OwnQQuickFolderDialog *>(self)->OwnQQuickFolderDialog::useNativeDialog();
}

//  void QQuickFolderDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickFolderDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFolderDialog *>(self)->OwnQQuickFolderDialog::onCreate(
      dialog);
}

//  void QQuickFolderDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickFolderDialog6onShowEP21QPlatformDialogHelper(
    QQuickFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFolderDialog *>(self)->OwnQQuickFolderDialog::onShow(
      dialog);
}
