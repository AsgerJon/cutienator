//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4generatorobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4vme_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4generatorobject.cpp, line 59, as _ZN3QV417GeneratorFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue GeneratorFunction::virtualCall(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    const GeneratorFunction *gf = static_cast<const GeneratorFunction *>(f);
    Function *function = gf->function();
    ExecutionEngine *engine = gf->engine();

    Scope scope(gf);
    Scoped<GeneratorObject> g(scope, engine->memoryManager->allocManaged<GeneratorObject>(engine->classes[EngineBase::Class_GeneratorObject]));
    g->setPrototypeOf(ScopedObject(scope, gf->get(scope.engine->id_prototype())));

    // We need to set up a separate JSFrame for the generator, as it's being re-entered
    Heap::GeneratorObject *gp = g->d();
    gp->values.set(engine, engine->newArrayObject(argc));
    gp->jsFrame.set(engine, engine->newArrayObject(
                        JSTypesStackFrame::requiredJSStackFrameSize(function)));

    // copy original arguments
    for (int i = 0; i < argc; i++)
        gp->values->arrayData->setArrayData(engine, i, argv[i]);

    gp->cppFrame.init(function, gp->values->arrayData->values.values, argc);
    gp->cppFrame.setupJSFrame(gp->jsFrame->arrayData->values.values, *gf, gf->scope(),
                              thisObject ? *thisObject : Value::undefinedValue(),
                              Value::undefinedValue());

    gp->cppFrame.push(engine);

    CHECK_STACK_LIMITS(scope.engine)
    Moth::VME::interpret(&gp->cppFrame, engine, function->codeData);

    gp->state = GeneratorState::SuspendedStart;

    gp->cppFrame.pop(engine);
    return g->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::MemberGeneratorFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV423MemberGeneratorFunction10__dataTestEv(
    QV4::MemberGeneratorFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::MemberGeneratorFunction
//      *QV4::MemberGeneratorFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberGeneratorFunction *ritual_ZNK3QV423MemberGeneratorFunction11d_uncheckedEv(
    const QV4::MemberGeneratorFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MemberGeneratorFunction *QV4::MemberGeneratorFunction::d()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberGeneratorFunction *ritual_ZNK3QV423MemberGeneratorFunction1dEv(
    const QV4::MemberGeneratorFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::MemberGeneratorFunction::defaultInternalClass(QV4::EngineBase
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV423MemberGeneratorFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::MemberGeneratorFunction::defaultInternalClass(e);
}
