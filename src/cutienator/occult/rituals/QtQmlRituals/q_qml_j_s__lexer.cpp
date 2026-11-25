//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljslexer_p.h, Qt 6.12.0, as the Qt of
//  macOS and of Windows install it, and that of Linux alike. Kept as
//  it is when the generator runs again.
//  Its header pulls in 'private/qqmljsgrammar_p.h', which Qt makes as it
//  builds and an installed Qt has. Not written: 'illegalFileLengthError',
//  which gives a 'std::optional', and 'scanChar' and 'peekChar', which
//  the header declares inline and never writes out.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljslexer_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>

//  QQmlJS::Lexer::Lexer(Engine *engine, LexMode lexMode)
extern "C" Q_DECL_EXPORT
QQmlJS::Lexer *ritual_ZN6QQmlJS5LexerC1EPNS_6EngineENS0_7LexModeE(
    QQmlJS::Engine *engine,
    QQmlJS::Lexer::LexMode lexMode) {
  return new QQmlJS::Lexer(engine, lexMode);
}

//  QQmlJS::Lexer::~Lexer()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5LexerD1Ev(QQmlJS::Lexer *self) {
  delete self;
}

//  bool QQmlJS::Lexer::qmlMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer7qmlModeEv(const QQmlJS::Lexer *self) {
  return self->qmlMode();
}

//  bool QQmlJS::Lexer::yieldIsKeyWord() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer14yieldIsKeyWordEv(const QQmlJS::Lexer *self) {
  return self->yieldIsKeyWord();
}

//  void QQmlJS::Lexer::setStaticIsKeyword(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer18setStaticIsKeywordEb(
    QQmlJS::Lexer *self,
    bool b) {
  self->setStaticIsKeyword(b);
}

//  QString QQmlJS::Lexer::code() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer4codeEv(const QQmlJS::Lexer *self) {
  return new QString(self->code());
}

//  void QQmlJS::Lexer::setCode(const QString &code, int lineno, bool
//      qmlMode, CodeContinuation codeContinuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer7setCodeERK7QStringibNS0_16CodeContinuationE(
    QQmlJS::Lexer *self,
    const QString *code,
    int lineno,
    bool qmlMode,
    QQmlJS::Lexer::CodeContinuation codeContinuation) {
  self->setCode(*code, lineno, qmlMode, codeContinuation);
}

//  int QQmlJS::Lexer::lex()
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer3lexEv(QQmlJS::Lexer *self) {
  return self->lex();
}

//  bool QQmlJS::Lexer::scanRegExp(RegExpBodyPrefix prefix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer10scanRegExpENS0_16RegExpBodyPrefixE(
    QQmlJS::Lexer *self,
    QQmlJS::Lexer::RegExpBodyPrefix prefix) {
  return self->scanRegExp(prefix);
}

//  bool QQmlJS::Lexer::scanDirectives(Directives *directives,
//      DiagnosticMessage *error)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer14scanDirectivesEPNS_10DirectivesEPNS_17DiagnosticMessageE(
    QQmlJS::Lexer *self,
    QQmlJS::Directives *directives,
    QQmlJS::DiagnosticMessage *error) {
  return self->scanDirectives(directives, error);
}

//  int QQmlJS::Lexer::regExpFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer11regExpFlagsEv(const QQmlJS::Lexer *self) {
  return self->regExpFlags();
}

//  QString QQmlJS::Lexer::regExpPattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer13regExpPatternEv(
    const QQmlJS::Lexer *self) {
  return new QString(self->regExpPattern());
}

//  int QQmlJS::Lexer::tokenKind() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer9tokenKindEv(const QQmlJS::Lexer *self) {
  return self->tokenKind();
}

//  int QQmlJS::Lexer::tokenOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer11tokenOffsetEv(const QQmlJS::Lexer *self) {
  return self->tokenOffset();
}

//  int QQmlJS::Lexer::tokenLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer11tokenLengthEv(const QQmlJS::Lexer *self) {
  return self->tokenLength();
}

//  int QQmlJS::Lexer::tokenStartLine() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer14tokenStartLineEv(const QQmlJS::Lexer *self) {
  return self->tokenStartLine();
}

//  int QQmlJS::Lexer::tokenStartColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer16tokenStartColumnEv(const QQmlJS::Lexer *self) {
  return self->tokenStartColumn();
}

//  QStringView QQmlJS::Lexer::tokenSpell() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer10tokenSpellEv(const QQmlJS::Lexer *self) {
  return new QString(self->tokenSpell().toString());
}

//  QStringView QQmlJS::Lexer::rawString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer9rawStringEv(const QQmlJS::Lexer *self) {
  return new QString(self->rawString().toString());
}

//  double QQmlJS::Lexer::tokenValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK6QQmlJS5Lexer10tokenValueEv(const QQmlJS::Lexer *self) {
  return self->tokenValue();
}

//  QString QQmlJS::Lexer::tokenText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer9tokenTextEv(const QQmlJS::Lexer *self) {
  return new QString(self->tokenText());
}

//  QQmlJS::Lexer::Error QQmlJS::Lexer::errorCode() const
extern "C" Q_DECL_EXPORT
QQmlJS::Lexer::Error ritual_ZNK6QQmlJS5Lexer9errorCodeEv(
    const QQmlJS::Lexer *self) {
  return self->errorCode();
}

//  QString QQmlJS::Lexer::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS5Lexer12errorMessageEv(const QQmlJS::Lexer *self) {
  return new QString(self->errorMessage());
}

//  bool QQmlJS::Lexer::canInsertAutomaticSemicolon(int token) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer27canInsertAutomaticSemicolonEi(
    const QQmlJS::Lexer *self,
    int token) {
  return self->canInsertAutomaticSemicolon(token);
}

//  void QQmlJS::Lexer::enterGeneratorBody()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer18enterGeneratorBodyEv(QQmlJS::Lexer *self) {
  self->enterGeneratorBody();
}

//  void QQmlJS::Lexer::leaveGeneratorBody()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer18leaveGeneratorBodyEv(QQmlJS::Lexer *self) {
  self->leaveGeneratorBody();
}

//  const State &QQmlJS::Lexer::state() const
extern "C" Q_DECL_EXPORT
QQmlJS::Lexer::State *ritual_ZNK6QQmlJS5Lexer5stateEv(
    const QQmlJS::Lexer *self) {
  return new QQmlJS::Lexer::State(self->state());
}

//  void QQmlJS::Lexer::setState(const State &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer8setStateERKNS0_5StateE(
    QQmlJS::Lexer *self,
    const QQmlJS::Lexer::State *state) {
  self->setState(*state);
}

//  int QQmlJS::Lexer::classify(QStringView s, int parseModeFlags)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer8classifyE11QStringViewi(
    const QString *s,
    int parseModeFlags) {
  return QQmlJS::Lexer::classify(QStringView(*s), parseModeFlags);
}

//  int QQmlJS::Lexer::parseModeFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS5Lexer14parseModeFlagsEv(const QQmlJS::Lexer *self) {
  return self->parseModeFlags();
}

//  bool QQmlJS::Lexer::prevTerminator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer14prevTerminatorEv(const QQmlJS::Lexer *self) {
  return self->prevTerminator();
}

//  bool QQmlJS::Lexer::followsClosingBrace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer19followsClosingBraceEv(
    const QQmlJS::Lexer *self) {
  return self->followsClosingBrace();
}

//  int QQmlJS::Lexer::scanToken()
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer9scanTokenEv(QQmlJS::Lexer *self) {
  return self->scanToken();
}

//  int QQmlJS::Lexer::scanNumber(QChar ch)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer10scanNumberE5QChar(
    QQmlJS::Lexer *self,
    const QChar *ch) {
  return self->scanNumber(*ch);
}

//  int QQmlJS::Lexer::scanVersionNumber(QChar ch)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer17scanVersionNumberE5QChar(
    QQmlJS::Lexer *self,
    const QChar *ch) {
  return self->scanVersionNumber(*ch);
}

//  int QQmlJS::Lexer::scanString(ScanStringMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QQmlJS5Lexer10scanStringENS0_14ScanStringModeE(
    QQmlJS::Lexer *self,
    QQmlJS::Lexer::ScanStringMode mode) {
  return self->scanString(mode);
}

//  bool QQmlJS::Lexer::isLineTerminator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS5Lexer16isLineTerminatorEv(const QQmlJS::Lexer *self) {
  return self->isLineTerminator();
}

//  unsigned QQmlJS::Lexer::isLineTerminatorSequence() const
extern "C" Q_DECL_EXPORT
unsigned ritual_ZNK6QQmlJS5Lexer24isLineTerminatorSequenceEv(
    const QQmlJS::Lexer *self) {
  return self->isLineTerminatorSequence();
}

//  bool QQmlJS::Lexer::isIdentLetter(QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer13isIdentLetterE5QChar(const QChar *c) {
  return QQmlJS::Lexer::isIdentLetter(*c);
}

//  bool QQmlJS::Lexer::isDecimalDigit(ushort c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer14isDecimalDigitEt(ushort c) {
  return QQmlJS::Lexer::isDecimalDigit(c);
}

//  bool QQmlJS::Lexer::isHexDigit(QChar c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer10isHexDigitE5QChar(const QChar *c) {
  return QQmlJS::Lexer::isHexDigit(*c);
}

//  bool QQmlJS::Lexer::isOctalDigit(ushort c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS5Lexer12isOctalDigitEt(ushort c) {
  return QQmlJS::Lexer::isOctalDigit(c);
}

//  void QQmlJS::Lexer::syncProhibitAutomaticSemicolon()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer30syncProhibitAutomaticSemicolonEv(
    QQmlJS::Lexer *self) {
  self->syncProhibitAutomaticSemicolon();
}

//  uint QQmlJS::Lexer::decodeUnicodeEscapeCharacter(bool *ok)
extern "C" Q_DECL_EXPORT
uint ritual_ZN6QQmlJS5Lexer28decodeUnicodeEscapeCharacterEPb(
    QQmlJS::Lexer *self,
    bool *ok) {
  return self->decodeUnicodeEscapeCharacter(ok);
}

//  QChar QQmlJS::Lexer::decodeHexEscapeCharacter(bool *ok)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN6QQmlJS5Lexer24decodeHexEscapeCharacterEPb(
    QQmlJS::Lexer *self,
    bool *ok) {
  return new QChar(self->decodeHexEscapeCharacter(ok));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const Lexer &l)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QQmlJSlsE6QDebugRKNS_5LexerE(
    const QDebug *dbg,
    const QQmlJS::Lexer *l) {
  return new QDebug(operator<<(*dbg, *l));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
