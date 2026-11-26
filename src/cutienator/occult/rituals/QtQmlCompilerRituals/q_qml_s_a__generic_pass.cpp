//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  'GenericPassPrivate' written in full as 'QQmlSA::GenericPassPrivate'
//  in the two 'd_func' rituals, as the compiler did not find the name
//  without its namespace. Kept as it is when the generator runs again.
#include <QtQmlCompiler/qqmlsa.h>

//  QQmlSA::GenericPassPrivate *QQmlSA::GenericPass::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::GenericPassPrivate *ritual_ZN6QQmlSA11GenericPass6d_funcEv(
    QQmlSA::GenericPass *self) {
  return self->d_func();
}

//  const QQmlSA::GenericPassPrivate *QQmlSA::GenericPass::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::GenericPassPrivate *ritual_ZNK6QQmlSA11GenericPass6d_funcEv(
    const QQmlSA::GenericPass *self) {
  return self->d_func();
}

//  QQmlSA::GenericPass::~GenericPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA11GenericPassD1Ev(QQmlSA::GenericPass *self) {
  delete self;
}
