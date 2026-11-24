//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const VirtualRegister &a, const VirtualRegister &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN17QQmlJSCompilePass15VirtualRegisterES2_(
    const QQmlJSCompilePass::VirtualRegister *a,
    const QQmlJSCompilePass::VirtualRegister *b) {
  return operator==(*a, *b);
}

//  QQmlJSCompilePass::VirtualRegister::~VirtualRegister()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15VirtualRegisterD1Ev(
    QQmlJSCompilePass::VirtualRegister *self) {
  delete self;
}
