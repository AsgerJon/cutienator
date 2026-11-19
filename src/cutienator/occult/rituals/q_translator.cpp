//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtranslator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtranslator.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>

//  const QMetaObject *QTranslator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTranslator10metaObjectEv(
    const QTranslator *self) {
  return self->metaObject();
}

//  QString QTranslator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTranslator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTranslator::tr(s, c, n));
}

//  QTranslator::QTranslator(QObject *parent)
extern "C" Q_DECL_EXPORT
QTranslator *ritual_ZN11QTranslatorC1EP7QObject(QObject *parent) {
  return new QTranslator(parent);
}

//  QTranslator::~QTranslator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTranslatorD1Ev(QTranslator *self) {
  delete self;
}

//  QString QTranslator::translate(const char *context, const char
//      *sourceText, const char *disambiguation, int n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator9translateEPKcS1_S1_i(
    const QTranslator *self,
    const char *context,
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      self->translate(
          context,
          sourceText,
          disambiguation,
          n));
}

//  bool QTranslator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTranslator7isEmptyEv(const QTranslator *self) {
  return self->isEmpty();
}

//  QString QTranslator::language() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator8languageEv(const QTranslator *self) {
  return new QString(self->language());
}

//  QString QTranslator::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator8filePathEv(const QTranslator *self) {
  return new QString(self->filePath());
}

//  bool QTranslator::load(const QString &filename, const QString &directory,
//      const QString &search_delimiters, const QString &suffix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTranslator4loadERK7QStringS2_S2_S2_(
    QTranslator *self,
    const QString *filename,
    const QString *directory,
    const QString *search_delimiters,
    const QString *suffix) {
  return self->load(*filename, *directory, *search_delimiters, *suffix);
}

//  bool QTranslator::load(const QLocale &locale, const QString &filename,
//      const QString &prefix, const QString &directory, const QString
//      &suffix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTranslator4loadERK7QLocaleRK7QStringS5_S5_S5_(
    QTranslator *self,
    const QLocale *locale,
    const QString *filename,
    const QString *prefix,
    const QString *directory,
    const QString *suffix) {
  return self->load(*locale, *filename, *prefix, *directory, *suffix);
}
