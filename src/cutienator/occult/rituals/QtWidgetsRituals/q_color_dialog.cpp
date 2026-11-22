//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcolordialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcolordialog.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QColorDialog10metaObjectEv(
    const QColorDialog *self) {
  return self->metaObject();
}

//  QString QColorDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QColorDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColorDialog::tr(s, c, n));
}

//  QColorDialog::QColorDialog(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColorDialog *ritual_ZN12QColorDialogC1EP7QWidget(QWidget *parent) {
  return new QColorDialog(parent);
}

//  QColorDialog::QColorDialog(const QColor &initial, QWidget *parent)
extern "C" Q_DECL_EXPORT
QColorDialog *ritual_ZN12QColorDialogC1ERK6QColorP7QWidget(
    const QColor *initial,
    QWidget *parent) {
  return new QColorDialog(*initial, parent);
}

//  QColorDialog::~QColorDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialogD1Ev(QColorDialog *self) {
  delete self;
}

//  void QColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog15setCurrentColorERK6QColor(
    QColorDialog *self,
    const QColor *color) {
  self->setCurrentColor(*color);
}

//  QColor QColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QColorDialog12currentColorEv(const QColorDialog *self) {
  return new QColor(self->currentColor());
}

//  QColor QColorDialog::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QColorDialog13selectedColorEv(const QColorDialog *self) {
  return new QColor(self->selectedColor());
}

//  void QColorDialog::setOption(ColorDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog9setOptionENS_17ColorDialogOptionEb(
    QColorDialog *self,
    QColorDialog::ColorDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QColorDialog::testOption(ColorDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorDialog10testOptionENS_17ColorDialogOptionE(
    const QColorDialog *self,
    QColorDialog::ColorDialogOption option) {
  return self->testOption(option);
}

//  void QColorDialog::setOptions(ColorDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog10setOptionsE6QFlagsINS_17ColorDialogOptionEE(
    QColorDialog *self,
    int options) {
  self->setOptions(
      QFlags<QColorDialog::ColorDialogOption>::fromInt(options));
}

//  ColorDialogOptions QColorDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QColorDialog7optionsEv(const QColorDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QColorDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog4openEP7QObjectPKc(
    QColorDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QColorDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog10setVisibleEb(
    QColorDialog *self,
    bool visible) {
  self->setVisible(visible);
}

//  QColor QColorDialog::getColor(const QColor &initial, QWidget *parent,
//      const QString &title, ColorDialogOptions options)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog8getColorERK6QColorP7QWidgetRK7QString6QFlagsINS_17ColorDialogOptionEE(
    const QColor *initial,
    QWidget *parent,
    const QString *title,
    int options) {
  return new QColor(
      QColorDialog::getColor(
          *initial,
          parent,
          *title,
          QFlags<QColorDialog::ColorDialogOption>::fromInt(options)));
}

//  int QColorDialog::customCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QColorDialog11customCountEv() {
  return QColorDialog::customCount();
}

//  QColor QColorDialog::customColor(int index)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog11customColorEi(int index) {
  return new QColor(QColorDialog::customColor(index));
}

//  void QColorDialog::setCustomColor(int index, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog14setCustomColorEi6QColor(
    int index,
    const QColor *color) {
  QColorDialog::setCustomColor(index, *color);
}

//  QColor QColorDialog::standardColor(int index)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog13standardColorEi(int index) {
  return new QColor(QColorDialog::standardColor(index));
}

//  void QColorDialog::setStandardColor(int index, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog16setStandardColorEi6QColor(
    int index,
    const QColor *color) {
  QColorDialog::setStandardColor(index, *color);
}
