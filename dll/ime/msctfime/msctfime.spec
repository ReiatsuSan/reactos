@ stdcall CtfImeDispatchDefImeMessage(ptr long ptr ptr)
@ stdcall CtfImeCreateInputContext(ptr)
@ stdcall CtfImeCreateThreadMgr()
@ stdcall CtfImeDestroyInputContext(ptr)
@ stdcall CtfImeDestroyThreadMgr()
@ stdcall CtfImeEscapeEx(ptr long ptr ptr)
@ stdcall CtfImeGetGuidAtom(ptr long ptr)
@ stdcall CtfImeInquireExW(ptr ptr long ptr)
@ stdcall CtfImeIsGuidMapEnable(ptr)
@ stdcall CtfImeIsIME(ptr)
@ stdcall CtfImeProcessCicHotkey(ptr long ptr)
@ stdcall CtfImeSelectEx(ptr long ptr)
@ stdcall CtfImeSetActiveContextAlways(ptr long ptr ptr)
@ stdcall CtfImeThreadDetach()
@ stdcall ImeConfigure(ptr ptr long ptr)
@ stdcall ImeConversionList(ptr wstr ptr long long)
@ stdcall ImeDestroy(long)
@ stdcall ImeEnumRegisterWord(ptr wstr long wstr ptr)
@ stdcall ImeEscape(ptr long ptr)
@ stdcall ImeGetRegisterWordStyle(long ptr)
@ stdcall ImeInquire(ptr ptr long)
@ stdcall ImeProcessKey(ptr long long ptr)
@ stdcall ImeRegisterWord(wstr long wstr)
@ stdcall ImeSelect(ptr long)
@ stdcall ImeSetActiveContext(ptr long)
@ stdcall ImeSetCompositionString(ptr long ptr long ptr long)
@ stdcall ImeToAsciiEx(long long ptr ptr long ptr)
@ stdcall ImeUnregisterWord(wstr long wstr)
@ stdcall NotifyIME(ptr long long long)
@ stdcall UIWndProc(ptr long ptr ptr)
