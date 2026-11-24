//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QFontDialogOptions::~QFontDialogOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogOptionsD1Ev(QFontDialogOptions *self) {
  delete self;
}

//  QString QFontDialogOptions::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFontDialogOptions11windowTitleEv(
    const QFontDialogOptions *self) {
  return new QString(self->windowTitle());
}

//  void QFontDialogOptions::setWindowTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogOptions14setWindowTitleERK7QString(
    QFontDialogOptions *self,
    const QString *a0) {
  self->setWindowTitle(*a0);
}

//  void QFontDialogOptions::setOption(FontDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogOptions9setOptionENS_16FontDialogOptionEb(
    QFontDialogOptions *self,
    QFontDialogOptions::FontDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFontDialogOptions::testOption(FontDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFontDialogOptions10testOptionENS_16FontDialogOptionE(
    const QFontDialogOptions *self,
    QFontDialogOptions::FontDialogOption option) {
  return self->testOption(option);
}

//  void QFontDialogOptions::setOptions(FontDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogOptions10setOptionsE6QFlagsINS_16FontDialogOptionEE(
    QFontDialogOptions *self,
    int options) {
  self->setOptions(
      QFlags<QFontDialogOptions::FontDialogOption>::fromInt(options));
}

//  FontDialogOptions QFontDialogOptions::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFontDialogOptions7optionsEv(
    const QFontDialogOptions *self) {
  return static_cast<int>(self->options().toInt());
}
