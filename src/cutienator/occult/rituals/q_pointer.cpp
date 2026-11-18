//  Written by hand. 'QPointer<QObject>' is a class the compiler makes
//  from Qt's pattern 'QPointer' in QtCore/qpointer.h, and
//  dev_tooling.RitualGenerator writes no rituals for patterns. Each ritual
//  is named as the generator would name it: 'ritual' and then the
//  compiler's own name for the Qt function it calls.
#include <QtCore/qobject.h>
#include <QtCore/qpointer.h>

//  QPointer<QObject>::QPointer(QObject *p)
extern "C" Q_DECL_EXPORT
QPointer<QObject> *ritual_ZN8QPointerI7QObjectEC1IvEEPS0_(QObject *p) {
  return new QPointer<QObject>(p);
}

//  QPointer<QObject>::~QPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPointerI7QObjectED1Ev(QPointer<QObject> *self) {
  delete self;
}

//  bool QPointer<QObject>::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPointerI7QObjectE6isNullEv(const QPointer<QObject> *self) {
  return self->isNull();
}
