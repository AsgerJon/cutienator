//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboarddictionary.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboarddictionary.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QVirtualKeyboardDictionary::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QVirtualKeyboardDictionary10metaObjectEv(
    const QVirtualKeyboardDictionary *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardDictionary::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QVirtualKeyboardDictionary2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardDictionary::tr(s, c, n));
}

//  QVirtualKeyboardDictionary::QVirtualKeyboardDictionary(const QString
//      &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardDictionary *ritual_ZN26QVirtualKeyboardDictionaryC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new QVirtualKeyboardDictionary(*name, parent);
}

//  QString QVirtualKeyboardDictionary::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QVirtualKeyboardDictionary4nameEv(
    const QVirtualKeyboardDictionary *self) {
  return new QString(self->name());
}

//  QStringList QVirtualKeyboardDictionary::contents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QVirtualKeyboardDictionary8contentsEv(
    const QVirtualKeyboardDictionary *self) {
  return new QList<QString>(self->contents());
}

//  void QVirtualKeyboardDictionary::setContents(const QStringList &contents)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QVirtualKeyboardDictionary11setContentsERK5QListI7QStringE(
    QVirtualKeyboardDictionary *self,
    const QList<QString> *contents) {
  self->setContents(*contents);
}

//  void QVirtualKeyboardDictionary::resetContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QVirtualKeyboardDictionary13resetContentsEv(
    QVirtualKeyboardDictionary *self) {
  self->resetContents();
}
