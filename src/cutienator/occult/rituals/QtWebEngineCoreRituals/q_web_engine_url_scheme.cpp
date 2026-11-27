//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineurlscheme.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebengineurlscheme.h>
#include <QtCore/qbytearray.h>

//  QWebEngineUrlScheme::QWebEngineUrlScheme()
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeC1Ev() {
  return new QWebEngineUrlScheme();
}

//  QWebEngineUrlScheme::QWebEngineUrlScheme(const QByteArray &name)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeC1ERK10QByteArray(
    const QByteArray *name) {
  return new QWebEngineUrlScheme(*name);
}

//  QWebEngineUrlScheme::QWebEngineUrlScheme(const QWebEngineUrlScheme &that)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeC1ERKS_(
    const QWebEngineUrlScheme *that) {
  return new QWebEngineUrlScheme(*that);
}

//  QWebEngineUrlScheme &QWebEngineUrlScheme::operator=(const
//      QWebEngineUrlScheme &that)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeaSERKS_(
    QWebEngineUrlScheme *self,
    const QWebEngineUrlScheme *that) {
  return &(self->operator=(*that));
}

//  QWebEngineUrlScheme::QWebEngineUrlScheme(QWebEngineUrlScheme &&that)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeC1EOS_(
    QWebEngineUrlScheme *that) {
  return new QWebEngineUrlScheme(std::move(*that));
}

//  QWebEngineUrlScheme &QWebEngineUrlScheme::operator=(QWebEngineUrlScheme
//      &&that)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeaSEOS_(
    QWebEngineUrlScheme *self,
    QWebEngineUrlScheme *that) {
  return &(self->operator=(std::move(*that)));
}

//  QWebEngineUrlScheme::~QWebEngineUrlScheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlSchemeD1Ev(QWebEngineUrlScheme *self) {
  delete self;
}

//  bool QWebEngineUrlScheme::operator==(const QWebEngineUrlScheme &that)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWebEngineUrlSchemeeqERKS_(
    const QWebEngineUrlScheme *self,
    const QWebEngineUrlScheme *that) {
  return self->operator==(*that);
}

//  bool QWebEngineUrlScheme::operator!=(const QWebEngineUrlScheme &that)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWebEngineUrlSchemeneERKS_(
    const QWebEngineUrlScheme *self,
    const QWebEngineUrlScheme *that) {
  return self->operator!=(*that);
}

//  QByteArray QWebEngineUrlScheme::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QWebEngineUrlScheme4nameEv(
    const QWebEngineUrlScheme *self) {
  return new QByteArray(self->name());
}

//  void QWebEngineUrlScheme::setName(const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme7setNameERK10QByteArray(
    QWebEngineUrlScheme *self,
    const QByteArray *newValue) {
  self->setName(*newValue);
}

//  Syntax QWebEngineUrlScheme::syntax() const
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme::Syntax ritual_ZNK19QWebEngineUrlScheme6syntaxEv(
    const QWebEngineUrlScheme *self) {
  return self->syntax();
}

//  void QWebEngineUrlScheme::setSyntax(Syntax newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme9setSyntaxENS_6SyntaxE(
    QWebEngineUrlScheme *self,
    QWebEngineUrlScheme::Syntax newValue) {
  self->setSyntax(newValue);
}

//  int QWebEngineUrlScheme::defaultPort() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWebEngineUrlScheme11defaultPortEv(
    const QWebEngineUrlScheme *self) {
  return self->defaultPort();
}

//  void QWebEngineUrlScheme::setDefaultPort(int newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme14setDefaultPortEi(
    QWebEngineUrlScheme *self,
    int newValue) {
  self->setDefaultPort(newValue);
}

//  Flags QWebEngineUrlScheme::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWebEngineUrlScheme5flagsEv(
    const QWebEngineUrlScheme *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QWebEngineUrlScheme::setFlags(Flags newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme8setFlagsE6QFlagsINS_4FlagEE(
    QWebEngineUrlScheme *self,
    int newValue) {
  self->setFlags(QFlags<QWebEngineUrlScheme::Flag>::fromInt(newValue));
}

//  void QWebEngineUrlScheme::registerScheme(const QWebEngineUrlScheme
//      &scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme14registerSchemeERKS_(
    const QWebEngineUrlScheme *scheme) {
  QWebEngineUrlScheme::registerScheme(*scheme);
}

//  QWebEngineUrlScheme QWebEngineUrlScheme::schemeByName(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlScheme12schemeByNameERK10QByteArray(
    const QByteArray *name) {
  return new QWebEngineUrlScheme(QWebEngineUrlScheme::schemeByName(*name));
}

//  void QWebEngineUrlScheme::lockSchemes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebEngineUrlScheme11lockSchemesEv() {
  QWebEngineUrlScheme::lockSchemes();
}

//  QWebEngineUrlScheme::QWebEngineUrlScheme(QWebEngineUrlSchemePrivate *d)
extern "C" Q_DECL_EXPORT
QWebEngineUrlScheme *ritual_ZN19QWebEngineUrlSchemeC1EP26QWebEngineUrlSchemePrivate(
    QWebEngineUrlSchemePrivate *d) {
  return new QWebEngineUrlScheme(d);
}
