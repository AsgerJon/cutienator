//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added State::accept, Transition::accept and
//  HistoryState::accept from Qt's source, as inline functions: Qt's library
//  carries them under no name, and the vtables the rituals need (newState,
//  newHistoryState, newTransition build these nodes) left them undefined
//  when linking. Kept as it is when the generator runs again. Also added by
//  hand on 2026-11-25, instances of templates of the class: 3.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlcompiler_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qfile.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#ifndef BUILD_QSCXMLC
#include <QtScxml/private/qscxmlinvokableservice_p.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/qscxmlstatemachine.h>
#include <QtScxml/private/qscxmltabledata_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1144, as _ZN13DocumentModel4NodeD2Ev
inline DocumentModel::Node::~Node()
{
}
//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1234, as _ZN13DocumentModel5State6acceptEPNS_11NodeVisitorE
inline void DocumentModel::State::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        visitor->visit(dataElements);
        visitor->visit(children);
        visitor->visit(onEntry);
        visitor->visit(onExit);
        if (doneData)
            doneData->accept(visitor);
        for (Invoke *invoke : std::as_const(invokes))
            invoke->accept(visitor);
    }
    visitor->endVisit(this);
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1249, as _ZN13DocumentModel10Transition6acceptEPNS_11NodeVisitorE
inline void DocumentModel::Transition::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        visitor->visit(&instructionsOnTransition);
    }
    visitor->endVisit(this);
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1257, as _ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisitorE
inline void DocumentModel::HistoryState::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        if (Transition *t = defaultConfiguration())
            t->accept(visitor);
    }
    visitor->endVisit(this);
}
//  -----------------------------------------------------------------------

//  DocumentModel::ScxmlDocument::ScxmlDocument(const QString &fileName)
extern "C" Q_DECL_EXPORT
DocumentModel::ScxmlDocument *ritual_ZN13DocumentModel13ScxmlDocumentC1ERK7QString(
    const QString *fileName) {
  return new DocumentModel::ScxmlDocument(*fileName);
}

//  DocumentModel::ScxmlDocument::~ScxmlDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel13ScxmlDocumentD1Ev(
    DocumentModel::ScxmlDocument *self) {
  delete self;
}

//  State *DocumentModel::ScxmlDocument::newState(StateContainer *parent,
//      State::Type type, const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_ZN13DocumentModel13ScxmlDocument8newStateEPNS_14StateContainerENS_5State4TypeERKNS_11XmlLocationE(
    DocumentModel::ScxmlDocument *self,
    DocumentModel::StateContainer *parent,
    DocumentModel::State::Type type,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newState(parent, type, *xmlLocation);
}

//  HistoryState
//      *DocumentModel::ScxmlDocument::newHistoryState(StateContainer
//      *parent, const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::HistoryState *ritual_ZN13DocumentModel13ScxmlDocument15newHistoryStateEPNS_14StateContainerERKNS_11XmlLocationE(
    DocumentModel::ScxmlDocument *self,
    DocumentModel::StateContainer *parent,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newHistoryState(parent, *xmlLocation);
}

//  Transition *DocumentModel::ScxmlDocument::newTransition(StateContainer
//      *parent, const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::Transition *ritual_ZN13DocumentModel13ScxmlDocument13newTransitionEPNS_14StateContainerERKNS_11XmlLocationE(
    DocumentModel::ScxmlDocument *self,
    DocumentModel::StateContainer *parent,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newTransition(parent, *xmlLocation);
}

//  InstructionSequence
//      *DocumentModel::ScxmlDocument::newSequence(InstructionSequences
//      *container)
extern "C" Q_DECL_EXPORT
DocumentModel::InstructionSequence *ritual_ZN13DocumentModel13ScxmlDocument11newSequenceEP5QListIPS1_IPNS_11InstructionEEE(
    DocumentModel::ScxmlDocument *self,
    DocumentModel::InstructionSequences *container) {
  return self->newSequence(container);
}

//  DocumentModel::State *DocumentModel::ScxmlDocument::newNode<
//      DocumentModel::State>(const DocumentModel::XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::State * ritual_ZN13DocumentModel13ScxmlDocument7newNodeINS_5StateEEEPT_RKNS_11XmlLocationE(DocumentModel::ScxmlDocument *self,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newNode<DocumentModel::State>(*xmlLocation);
}

//  DocumentModel::HistoryState *DocumentModel::ScxmlDocument::newNode<
//      DocumentModel::HistoryState>(const DocumentModel::XmlLocation
//      &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::HistoryState * ritual_ZN13DocumentModel13ScxmlDocument7newNodeINS_12HistoryStateEEEPT_RKNS_11XmlLocationE(DocumentModel::ScxmlDocument *self,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newNode<DocumentModel::HistoryState>(*xmlLocation);
}

//  DocumentModel::Transition *DocumentModel::ScxmlDocument::newNode<
//      DocumentModel::Transition>(const DocumentModel::XmlLocation
//      &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::Transition * ritual_ZN13DocumentModel13ScxmlDocument7newNodeINS_10TransitionEEEPT_RKNS_11XmlLocationE(DocumentModel::ScxmlDocument *self,
    const DocumentModel::XmlLocation *xmlLocation) {
  return self->newNode<DocumentModel::Transition>(*xmlLocation);
}
