//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcualocalizedtext.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QOpcUaLocalizedText::QOpcUaLocalizedText()
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZN19QOpcUaLocalizedTextC1Ev() {
  return new QOpcUaLocalizedText();
}

//  QOpcUaLocalizedText::QOpcUaLocalizedText(const QOpcUaLocalizedText &a0)
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZN19QOpcUaLocalizedTextC1ERKS_(
    const QOpcUaLocalizedText *a0) {
  return new QOpcUaLocalizedText(*a0);
}

//  QOpcUaLocalizedText::QOpcUaLocalizedText(const QString &locale, const
//      QString &text)
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZN19QOpcUaLocalizedTextC1ERK7QStringS2_(
    const QString *locale,
    const QString *text) {
  return new QOpcUaLocalizedText(*locale, *text);
}

//  bool QOpcUaLocalizedText::operator==(const QOpcUaLocalizedText &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaLocalizedTexteqERKS_(
    const QOpcUaLocalizedText *self,
    const QOpcUaLocalizedText *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaLocalizedText::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QOpcUaLocalizedTextcv8QVariantEv(
    const QOpcUaLocalizedText *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaLocalizedText::~QOpcUaLocalizedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaLocalizedTextD1Ev(QOpcUaLocalizedText *self) {
  delete self;
}

//  QString QOpcUaLocalizedText::locale() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpcUaLocalizedText6localeEv(
    const QOpcUaLocalizedText *self) {
  return new QString(self->locale());
}

//  void QOpcUaLocalizedText::setLocale(const QString &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaLocalizedText9setLocaleERK7QString(
    QOpcUaLocalizedText *self,
    const QString *locale) {
  self->setLocale(*locale);
}

//  QString QOpcUaLocalizedText::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpcUaLocalizedText4textEv(
    const QOpcUaLocalizedText *self) {
  return new QString(self->text());
}

//  void QOpcUaLocalizedText::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaLocalizedText7setTextERK7QString(
    QOpcUaLocalizedText *self,
    const QString *text) {
  self->setText(*text);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QOpcUaLocalizedText &lt)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QOpcUaLocalizedText(
    const QDebug *debug,
    const QOpcUaLocalizedText *lt) {
  return new QDebug(operator<<(*debug, *lt));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QOpcUaLocalizedText>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaLocalizedText> *ritual_list_make_QOpcUaLocalizedText() {
  return new QList<QOpcUaLocalizedText>();
}

//  void QList<QOpcUaLocalizedText>::append(const QOpcUaLocalizedText &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaLocalizedText(
    QList<QOpcUaLocalizedText> *self,
    const QOpcUaLocalizedText *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaLocalizedText>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaLocalizedText(
    const QList<QOpcUaLocalizedText> *self) {
  return self->size();
}

//  const QOpcUaLocalizedText &QList<QOpcUaLocalizedText>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_list_at_QOpcUaLocalizedText(
    const QList<QOpcUaLocalizedText> *self,
    long long index) {
  return new QOpcUaLocalizedText(self->at(index));
}

//  QList<QOpcUaLocalizedText>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaLocalizedText(QList<QOpcUaLocalizedText> *self) {
  delete self;
}
