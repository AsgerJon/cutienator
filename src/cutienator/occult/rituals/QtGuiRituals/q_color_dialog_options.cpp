//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QColorDialogOptions::~QColorDialogOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptionsD1Ev(QColorDialogOptions *self) {
  delete self;
}

//  QString QColorDialogOptions::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QColorDialogOptions11windowTitleEv(
    const QColorDialogOptions *self) {
  return new QString(self->windowTitle());
}

//  void QColorDialogOptions::setWindowTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptions14setWindowTitleERK7QString(
    QColorDialogOptions *self,
    const QString *a0) {
  self->setWindowTitle(*a0);
}

//  void QColorDialogOptions::setOption(ColorDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptions9setOptionENS_17ColorDialogOptionEb(
    QColorDialogOptions *self,
    QColorDialogOptions::ColorDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QColorDialogOptions::testOption(ColorDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QColorDialogOptions10testOptionENS_17ColorDialogOptionE(
    const QColorDialogOptions *self,
    QColorDialogOptions::ColorDialogOption option) {
  return self->testOption(option);
}

//  void QColorDialogOptions::setOptions(ColorDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptions10setOptionsE6QFlagsINS_17ColorDialogOptionEE(
    QColorDialogOptions *self,
    int options) {
  self->setOptions(
      QFlags<QColorDialogOptions::ColorDialogOption>::fromInt(options));
}

//  ColorDialogOptions QColorDialogOptions::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QColorDialogOptions7optionsEv(
    const QColorDialogOptions *self) {
  return static_cast<int>(self->options().toInt());
}

//  int QColorDialogOptions::customColorCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QColorDialogOptions16customColorCountEv() {
  return QColorDialogOptions::customColorCount();
}

//  QRgb QColorDialogOptions::customColor(int index)
extern "C" Q_DECL_EXPORT
QRgb ritual_ZN19QColorDialogOptions11customColorEi(int index) {
  return QColorDialogOptions::customColor(index);
}

//  void QColorDialogOptions::setCustomColor(int index, QRgb color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptions14setCustomColorEij(
    int index,
    QRgb color) {
  QColorDialogOptions::setCustomColor(index, color);
}

//  QRgb QColorDialogOptions::standardColor(int index)
extern "C" Q_DECL_EXPORT
QRgb ritual_ZN19QColorDialogOptions13standardColorEi(int index) {
  return QColorDialogOptions::standardColor(index);
}

//  void QColorDialogOptions::setStandardColor(int index, QRgb color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorDialogOptions16setStandardColorEij(
    int index,
    QRgb color) {
  QColorDialogOptions::setStandardColor(index, color);
}
