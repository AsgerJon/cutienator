//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljsengine_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: it has no
//  virtual function and its functions are all inline. Not written: the
//  constructor, and 'comments', which gives a QList.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsengine_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  void QQmlJS::Engine::setCode(const QString &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine7setCodeERK7QString(
    QQmlJS::Engine *self,
    const QString *code) {
  self->setCode(*code);
}

//  const QString &QQmlJS::Engine::code() const
extern "C" Q_DECL_EXPORT
const QString *ritual_ZNK6QQmlJS6Engine4codeEv(
    const QQmlJS::Engine *self) {
  return &(self->code());
}

//  void QQmlJS::Engine::addComment(int pos, int len, int line, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine10addCommentEiiii(
    QQmlJS::Engine *self,
    int pos,
    int len,
    int line,
    int col) {
  self->addComment(pos, len, line, col);
}

//  Lexer *QQmlJS::Engine::lexer() const
extern "C" Q_DECL_EXPORT
QQmlJS::Lexer *ritual_ZNK6QQmlJS6Engine5lexerEv(
    const QQmlJS::Engine *self) {
  return self->lexer();
}

//  void QQmlJS::Engine::setLexer(Lexer *lexer)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine8setLexerEPNS_5LexerE(
    QQmlJS::Engine *self,
    QQmlJS::Lexer *lexer) {
  self->setLexer(lexer);
}

//  Directives *QQmlJS::Engine::directives() const
extern "C" Q_DECL_EXPORT
QQmlJS::Directives *ritual_ZNK6QQmlJS6Engine10directivesEv(
    const QQmlJS::Engine *self) {
  return self->directives();
}

//  void QQmlJS::Engine::setDirectives(Directives *directives)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine13setDirectivesEPNS_10DirectivesE(
    QQmlJS::Engine *self,
    QQmlJS::Directives *directives) {
  self->setDirectives(directives);
}

//  MemoryPool *QQmlJS::Engine::pool()
extern "C" Q_DECL_EXPORT
QQmlJS::MemoryPool *ritual_ZN6QQmlJS6Engine4poolEv(
    QQmlJS::Engine *self) {
  return self->pool();
}

//  const MemoryPool *QQmlJS::Engine::pool() const
extern "C" Q_DECL_EXPORT
const QQmlJS::MemoryPool *ritual_ZNK6QQmlJS6Engine4poolEv(
    const QQmlJS::Engine *self) {
  return self->pool();
}

//  QStringView QQmlJS::Engine::midRef(int position, int size)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN6QQmlJS6Engine6midRefEii(
    QQmlJS::Engine *self,
    int position,
    int size) {
  return new QStringView(self->midRef(position, size));
}

//  QStringView QQmlJS::Engine::newStringRef(const QString &text)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN6QQmlJS6Engine12newStringRefERK7QString(
    QQmlJS::Engine *self,
    const QString *text) {
  return new QStringView(self->newStringRef(*text));
}

//  QStringView QQmlJS::Engine::newStringRef(const QChar *chars, int
//      size)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN6QQmlJS6Engine12newStringRefEPK5QChari(
    QQmlJS::Engine *self,
    const QChar *chars,
    int size) {
  return new QStringView(self->newStringRef(chars, size));
}
