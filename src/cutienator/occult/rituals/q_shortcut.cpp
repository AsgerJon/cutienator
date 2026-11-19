//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qshortcut.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qshortcut.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QShortcut::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QShortcut10metaObjectEv(
    const QShortcut *self) {
  return self->metaObject();
}

//  QString QShortcut::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QShortcut2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QShortcut::tr(s, c, n));
}

//  QShortcut::QShortcut(QObject *parent)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1EP7QObject(QObject *parent) {
  return new QShortcut(parent);
}

//  QShortcut::QShortcut(const QKeySequence &key, QObject *parent, const char
//      *member, const char *ambiguousMember, Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1ERK12QKeySequenceP7QObjectPKcS6_N2Qt15ShortcutContextE(
    const QKeySequence *key,
    QObject *parent,
    const char *member,
    const char *ambiguousMember,
    Qt::ShortcutContext context) {
  return new QShortcut(*key, parent, member, ambiguousMember, context);
}

//  QShortcut::QShortcut(QKeySequence::StandardKey key, QObject *parent,
//      const char *member, const char *ambiguousMember, Qt::ShortcutContext
//      context)
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN9QShortcutC1EN12QKeySequence11StandardKeyEP7QObjectPKcS5_N2Qt15ShortcutContextE(
    QKeySequence::StandardKey key,
    QObject *parent,
    const char *member,
    const char *ambiguousMember,
    Qt::ShortcutContext context) {
  return new QShortcut(key, parent, member, ambiguousMember, context);
}

//  QShortcut::~QShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcutD1Ev(QShortcut *self) {
  delete self;
}

//  void QShortcut::setKey(const QKeySequence &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut6setKeyERK12QKeySequence(
    QShortcut *self,
    const QKeySequence *key) {
  self->setKey(*key);
}

//  QKeySequence QShortcut::key() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK9QShortcut3keyEv(const QShortcut *self) {
  return new QKeySequence(self->key());
}

//  void QShortcut::setKeys(QKeySequence::StandardKey key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut7setKeysEN12QKeySequence11StandardKeyE(
    QShortcut *self,
    QKeySequence::StandardKey key) {
  self->setKeys(key);
}

//  void QShortcut::setEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut10setEnabledEb(QShortcut *self, bool enable) {
  self->setEnabled(enable);
}

//  bool QShortcut::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QShortcut9isEnabledEv(const QShortcut *self) {
  return self->isEnabled();
}

//  void QShortcut::setContext(Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut10setContextEN2Qt15ShortcutContextE(
    QShortcut *self,
    Qt::ShortcutContext context) {
  self->setContext(context);
}

//  Qt::ShortcutContext QShortcut::context() const
extern "C" Q_DECL_EXPORT
Qt::ShortcutContext ritual_ZNK9QShortcut7contextEv(const QShortcut *self) {
  return self->context();
}

//  void QShortcut::setAutoRepeat(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut13setAutoRepeatEb(QShortcut *self, bool on) {
  self->setAutoRepeat(on);
}

//  bool QShortcut::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QShortcut10autoRepeatEv(const QShortcut *self) {
  return self->autoRepeat();
}

//  int QShortcut::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QShortcut2idEv(const QShortcut *self) {
  return self->id();
}

//  void QShortcut::setWhatsThis(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QShortcut12setWhatsThisERK7QString(
    QShortcut *self,
    const QString *text) {
  self->setWhatsThis(*text);
}

//  QString QShortcut::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QShortcut9whatsThisEv(const QShortcut *self) {
  return new QString(self->whatsThis());
}
