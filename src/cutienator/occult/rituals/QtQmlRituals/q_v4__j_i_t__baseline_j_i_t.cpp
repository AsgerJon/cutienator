//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4baselinejit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_jit)
#if QT_CONFIG(qml_jit)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4baselinejit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4baselinejit_p.h>
#include <QtQml/private/qv4baselineassembler_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4generatorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jit/qv4baselineassembler.cpp, line 791, as local:qv4baselineassembler.cpp:pasm
#if QT_CONFIG(qml_jit)
#define pasm() reinterpret_cast<PlatformAssembler *>(this->d)
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 44, as local:qv4baselinejit.cpp:STORE_IP
#if QT_CONFIG(qml_jit)
#define STORE_IP() as->storeInstructionPointer(nextInstructionOffset())
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 45, as local:qv4baselinejit.cpp:STORE_ACC
#if QT_CONFIG(qml_jit)
#define STORE_ACC() as->saveAccumulatorInFrame()
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 448, as _ZN3QV43JIT11BaselineJIT17generate_TailCallEiiii
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::generate_TailCall(int func, int thisObject, int argc, int argv)
{
    STORE_IP();
    as->jsTailCall(func, thisObject, argc, argv);
}
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 58, as _ZN3QV43JIT11BaselineJIT14generate_DebugEv
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::generate_Debug() { Q_UNREACHABLE(); }
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 328, as _ZN3QV43JIT11BaselineJIT14generate_YieldEv
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::generate_Yield()
{
    // #####
    Q_UNREACHABLE();
}
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 334, as _ZN3QV43JIT11BaselineJIT18generate_YieldStarEv
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::generate_YieldStar()
{
    // #####
    Q_UNREACHABLE();
}
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 340, as _ZN3QV43JIT11BaselineJIT15generate_ResumeEi
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::generate_Resume(int)
{
    // #####
    Q_UNREACHABLE();
}
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)

//  from ../qtdeclarative/src/qml/jit/qv4baselinejit.cpp, line 915, as _ZN3QV43JIT11BaselineJIT14endInstructionENS_4Moth5Instr4TypeE
#if QT_CONFIG(qml_jit)
namespace QV4::JIT {
using namespace QV4;
using namespace QV4::Moth;
inline void BaselineJIT::endInstruction(Instr::Type instr)
{
    Q_UNUSED(instr);
}
}  // namespace QV4::JIT
#endif  // QT_CONFIG(qml_jit)
//  -----------------------------------------------------------------------

#if QT_CONFIG(qml_jit)
//  void QV4::JIT::BaselineJIT::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV43JIT11BaselineJIT14generate_DebugEv(
    QV4::JIT::BaselineJIT *self) {
  self->generate_Debug();
}
#endif  // QT_CONFIG(qml_jit)

#if QT_CONFIG(qml_jit)
//  void QV4::JIT::BaselineJIT::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV43JIT11BaselineJIT14generate_YieldEv(
    QV4::JIT::BaselineJIT *self) {
  self->generate_Yield();
}
#endif  // QT_CONFIG(qml_jit)

#if QT_CONFIG(qml_jit)
//  void QV4::JIT::BaselineJIT::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV43JIT11BaselineJIT18generate_YieldStarEv(
    QV4::JIT::BaselineJIT *self) {
  self->generate_YieldStar();
}
#endif  // QT_CONFIG(qml_jit)

#if QT_CONFIG(qml_jit)
//  void QV4::JIT::BaselineJIT::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV43JIT11BaselineJIT15generate_ResumeEi(
    QV4::JIT::BaselineJIT *self,
    int a0) {
  self->generate_Resume(a0);
}
#endif  // QT_CONFIG(qml_jit)

#if QT_CONFIG(qml_jit)
//  void QV4::JIT::BaselineJIT::endInstruction(Moth::Instr::Type instr)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV43JIT11BaselineJIT14endInstructionENS_4Moth5Instr4TypeE(
    QV4::JIT::BaselineJIT *self,
    QV4::Moth::Instr::Type instr) {
  self->endInstruction(instr);
}
#endif  // QT_CONFIG(qml_jit)

#endif  // QT_CONFIG(qml_jit)
#endif  // QT_CONFIG(qml_jit)
