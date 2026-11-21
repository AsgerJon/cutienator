//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfontcombobox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfontcombobox.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QFontComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QFontComboBox10metaObjectEv(
    const QFontComboBox *self) {
  return self->metaObject();
}

//  QString QFontComboBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontComboBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFontComboBox::tr(s, c, n));
}

//  QFontComboBox::QFontComboBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontComboBox *ritual_ZN13QFontComboBoxC1EP7QWidget(QWidget *parent) {
  return new QFontComboBox(parent);
}

//  QFontComboBox::~QFontComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBoxD1Ev(QFontComboBox *self) {
  delete self;
}

//  void QFontComboBox::setWritingSystem(QFontDatabase::WritingSystem a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox16setWritingSystemEN13QFontDatabase13WritingSystemE(
    QFontComboBox *self,
    QFontDatabase::WritingSystem a0) {
  self->setWritingSystem(a0);
}

//  QFontDatabase::WritingSystem QFontComboBox::writingSystem() const
extern "C" Q_DECL_EXPORT
QFontDatabase::WritingSystem ritual_ZNK13QFontComboBox13writingSystemEv(
    const QFontComboBox *self) {
  return self->writingSystem();
}

//  void QFontComboBox::setFontFilters(FontFilters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setFontFiltersE6QFlagsINS_10FontFilterEE(
    QFontComboBox *self,
    int filters) {
  self->setFontFilters(QFlags<QFontComboBox::FontFilter>::fromInt(filters));
}

//  FontFilters QFontComboBox::fontFilters() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontComboBox11fontFiltersEv(const QFontComboBox *self) {
  return static_cast<int>(self->fontFilters().toInt());
}

//  QFont QFontComboBox::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QFontComboBox11currentFontEv(const QFontComboBox *self) {
  return new QFont(self->currentFont());
}

//  QSize QFontComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QFontComboBox8sizeHintEv(const QFontComboBox *self) {
  return new QSize(self->sizeHint());
}

//  void QFontComboBox::setSampleTextForSystem(QFontDatabase::WritingSystem
//      writingSystem, const QString &sampleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox22setSampleTextForSystemEN13QFontDatabase13WritingSystemERK7QString(
    QFontComboBox *self,
    QFontDatabase::WritingSystem writingSystem,
    const QString *sampleText) {
  self->setSampleTextForSystem(writingSystem, *sampleText);
}

//  QString QFontComboBox::sampleTextForSystem(QFontDatabase::WritingSystem
//      writingSystem) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontComboBox19sampleTextForSystemEN13QFontDatabase13WritingSystemE(
    const QFontComboBox *self,
    QFontDatabase::WritingSystem writingSystem) {
  return new QString(self->sampleTextForSystem(writingSystem));
}

//  void QFontComboBox::setSampleTextForFont(const QString &fontFamily, const
//      QString &sampleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox20setSampleTextForFontERK7QStringS2_(
    QFontComboBox *self,
    const QString *fontFamily,
    const QString *sampleText) {
  self->setSampleTextForFont(*fontFamily, *sampleText);
}

//  QString QFontComboBox::sampleTextForFont(const QString &fontFamily) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontComboBox17sampleTextForFontERK7QString(
    const QFontComboBox *self,
    const QString *fontFamily) {
  return new QString(self->sampleTextForFont(*fontFamily));
}

//  void QFontComboBox::setDisplayFont(const QString &fontFamily, const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setDisplayFontERK7QStringRK5QFont(
    QFontComboBox *self,
    const QString *fontFamily,
    const QFont *font) {
  self->setDisplayFont(*fontFamily, *font);
}

//  void QFontComboBox::setCurrentFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setCurrentFontERK5QFont(
    QFontComboBox *self,
    const QFont *f) {
  self->setCurrentFont(*f);
}
