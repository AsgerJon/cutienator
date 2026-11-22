//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfontdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfontdialog.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFontDialog10metaObjectEv(
    const QFontDialog *self) {
  return self->metaObject();
}

//  QString QFontDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFontDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFontDialog::tr(s, c, n));
}

//  QFontDialog::QFontDialog(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontDialog *ritual_ZN11QFontDialogC1EP7QWidget(QWidget *parent) {
  return new QFontDialog(parent);
}

//  QFontDialog::QFontDialog(const QFont &initial, QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontDialog *ritual_ZN11QFontDialogC1ERK5QFontP7QWidget(
    const QFont *initial,
    QWidget *parent) {
  return new QFontDialog(*initial, parent);
}

//  QFontDialog::~QFontDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialogD1Ev(QFontDialog *self) {
  delete self;
}

//  void QFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog14setCurrentFontERK5QFont(
    QFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}

//  QFont QFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QFontDialog11currentFontEv(const QFontDialog *self) {
  return new QFont(self->currentFont());
}

//  QFont QFontDialog::selectedFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QFontDialog12selectedFontEv(const QFontDialog *self) {
  return new QFont(self->selectedFont());
}

//  void QFontDialog::setOption(FontDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog9setOptionENS_16FontDialogOptionEb(
    QFontDialog *self,
    QFontDialog::FontDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFontDialog::testOption(FontDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontDialog10testOptionENS_16FontDialogOptionE(
    const QFontDialog *self,
    QFontDialog::FontDialogOption option) {
  return self->testOption(option);
}

//  void QFontDialog::setOptions(FontDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog10setOptionsE6QFlagsINS_16FontDialogOptionEE(
    QFontDialog *self,
    int options) {
  self->setOptions(QFlags<QFontDialog::FontDialogOption>::fromInt(options));
}

//  FontDialogOptions QFontDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFontDialog7optionsEv(const QFontDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QFontDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog4openEP7QObjectPKc(
    QFontDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QFontDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog10setVisibleEb(QFontDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QFont QFontDialog::getFont(bool *ok, QWidget *parent)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN11QFontDialog7getFontEPbP7QWidget(
    bool *ok,
    QWidget *parent) {
  return new QFont(QFontDialog::getFont(ok, parent));
}

//  QFont QFontDialog::getFont(bool *ok, const QFont &initial, QWidget
//      *parent, const QString &title, FontDialogOptions options)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN11QFontDialog7getFontEPbRK5QFontP7QWidgetRK7QString6QFlagsINS_16FontDialogOptionEE(
    bool *ok,
    const QFont *initial,
    QWidget *parent,
    const QString *title,
    int options) {
  return new QFont(
      QFontDialog::getFont(
          ok,
          *initial,
          parent,
          *title,
          QFlags<QFontDialog::FontDialogOption>::fromInt(options)));
}
