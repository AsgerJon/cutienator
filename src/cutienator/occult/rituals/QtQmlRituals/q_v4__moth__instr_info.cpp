//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4instr_moth_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4calldata_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/compiler/qv4instr_moth.cpp, line 14, as _ZN3QV44Moth9InstrInfo4sizeENS0_5Instr4TypeE
namespace QV4::Moth {
using namespace QV4;
inline int InstrInfo::size(Instr::Type type)
{
#define MOTH_RETURN_INSTR_SIZE(I) case Instr::Type::I: case Instr::Type::I##_Wide: return InstrMeta<int(Instr::Type::I)>::Size;
    switch (type) {
    FOR_EACH_MOTH_INSTR_ALL(MOTH_RETURN_INSTR_SIZE)
    }
#undef MOTH_RETURN_INSTR_SIZE
    Q_UNREACHABLE();
}
}  // namespace QV4::Moth
//  -----------------------------------------------------------------------

//  int QV4::Moth::InstrInfo::size(Instr::Type type)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV44Moth9InstrInfo4sizeENS0_5Instr4TypeE(
    QV4::Moth::Instr::Type type) {
  return QV4::Moth::InstrInfo::size(type);
}

//  QV4::Moth::InstrInfo::~InstrInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth9InstrInfoD1Ev(QV4::Moth::InstrInfo *self) {
  delete self;
}
